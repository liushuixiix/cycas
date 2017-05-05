#!/bin/env python
# -*- coding=utf-8 -*-
import cv2

catPath = "haarcascades/haarcascade_frontalcatface.xml"
faceCascade = cv2.CascadeClassifier(catPath)


def hasCat(img, scale=(1.3, 3, (350, 350))):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 猫脸检测
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=scale[0],
        minNeighbors=scale[1],
        minSize=scale[2],
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return faces

def pointCats(img, faces, name='01'):
    if faces is not ():
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img,'Cat',(x,y-7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imwrite(name + ".jpg", img)
    # print(faces)
    return img


def videoGen(vname, vstep=5):
    videoCapture = cv2.VideoCapture(vname)

    fps = videoCapture.get(cv2.CAP_PROP_FPS)

    def timer():
        i = 1
        while True:
            yield i
            i += 1

    success, frame = videoCapture.read()
    t = timer()
    curtime = 0
    receive = -1

    while success and receive == -1:
        if receive == 0:
            pass
        receive = yield frame, curtime
        for i in range(int(vstep)):
            success, frame = videoCapture.read()
            curtime = t.__next__() / fps
    else:
        yield None, t.__next__() / fps


def test_hasCat():
    for i in range(1, 11):
        imgname = "testpic/cat{0}.jpg".format(i)
        img = cv2.imread(imgname)
        scale = (1.05, 22, (175, 175))
        faces = hasCat(img, scale)
        img = pointCats(img, faces)
        cv2.imshow('Cat?', img)
        cv2.waitKey(0)

def test_videoGen():
    video = videoGen('testvideo\\01.mp4', 25)
    img, curtime = video.send(None)
    while img is not None:
        cv2.imshow('Cat?', img)
        img, curtime= video.send(cv2.waitKey(1))
        print(curtime)


def test_videohasCat():
    video = videoGen('testvideo\\01.mp4', 18)
    img, curtime = video.send(None)
    while img is not None:
        scale = (1.05, 22, (175, 175))
        faces = hasCat(img, scale)
        img = pointCats(img, faces, str(curtime))
        cv2.imshow('Cat?', img)
        img, curtime= video.send(cv2.waitKey(1))
        print(curtime)


if __name__ == '__main__':
    test_videohasCat()
