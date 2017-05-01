#!/bin/env python
# -*- coding=utf-8 -*-
import cv2

catPath = "haarcascades/haarcascade_frontalcatface.xml"
faceCascade = cv2.CascadeClassifier(catPath)


def hasCat(imgName, scale=(1.3, 3, (350, 350))):
    img = cv2.imread(imgName)
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

def showCats(img, faces):
    img = cv2.imread(img)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img,'Cat',(x,y-7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)
    print(faces)
    cv2.imshow('Cat?', img)
    # cv2.imwrite("cat.jpg",img)
    c = cv2.waitKey(0)

def test():
    for i in range(1, 11):
        imgname = "testpic/cat{0}.jpg".format(i)
        scale = (1.05, 22, (175, 175))
        faces = hasCat(imgname, scale)
        showCats(imgname, faces)

if __name__ == '__main__':
    test()
