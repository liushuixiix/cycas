# -*- coding: utf-8 -*-
# 使用OpenCV播放视频
import cv2

wnd = 'OpenCV Video'

# 获得视频的格式
videoCapture = cv2.VideoCapture('testvideo\\01.mp4')

# 获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

cv2.namedWindow(wnd, flags=0)
cv2.resizeWindow(wnd, size[0], size[1])

def timer():
    i = 1
    while True:
        yield i
        i += 1

t = timer()

def videogen(fps):
    # 读帧
    success, frame = videoCapture.read()
    receive = -1
    while success and receive == -1:
        receive = yield frame
        # print(t.__next__())
        for i in range(int(fps)):
            success, frame = videoCapture.read()  # 获取下一帧
    else:
        yield None


video = videogen(fps)
img = video.send(None)
while img is not None:
    cv2.imshow(wnd, img)
    img = video.send(cv2.waitKey(1))