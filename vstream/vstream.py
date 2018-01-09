# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
cap.release()

def capture():
    cap = cv2.VideoCapture(0)
    while(1):
        #print('[VSTREAM] Capturing Video……')
        #while cap.isOpened():
        ok1,frame=cap.read()
        if not ok1:break                    
        cv2.imshow('Capturing', frame)
        c=cv2.waitKey(10)
        if c & 0xFF == ord('q'):break    
    cap.release()
    cv2.destroyAllWindows() 
        
if __name__=='__main__':
    capture()