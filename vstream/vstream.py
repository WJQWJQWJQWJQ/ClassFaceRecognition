# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

def capture():
    while(1):
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):break
        cap.release()
        cv2.destroyAllWindows() 