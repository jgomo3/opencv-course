#!/usr/bin/env python

import cv2 as cv

def read_image():
    img = cv.imread('Photos/cat.jpg')
    # img = cv.imread('Photos/cat_large.jpg')
    # img = cv.imread('Photos/wrong_file')
    cv.imshow('Cat', img)
    cv.waitKey(0)

def read_video():
    capture = cv.VideoCapture('Videos/dog.mp4')
    while True:
        isTrue, frame = capture.read()
        cv.imshow('Video', frame)
        
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()
        
    cv.destroyAllWindows()
    
if __name__ == '__main__':
    # read_image()
    read_video()
