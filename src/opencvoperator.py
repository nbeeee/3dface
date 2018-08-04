#!/usr/bin/python

import dlib
import numpy as np
import cv2
import os


detector = dlib.get_frontal_face_detector()
facepath = 'face/face.jpg'
def faceDetector(frame):
    if os.path.exists(facepath):
        os.remove(facepath)
    dets = detector(frame, 1)
    print("Number of faces detected: {}".format(len(dets)))
    if(len(dets) == 0): return

    face = dets[0]

    # 计算矩形框大小
    height = face.bottom()
    width = face.right()
    box = np.zeros((height, width, 3), np.uint8)
    for i in range(height):
        for j in range(width):
            box[i][j] = frame[i][int(face.left() /2) + j]

    cv2.imwrite('face/face.jpg',box)




