import cv2 as cv
import numpy as np

img = cv.imread('Photos/lady.jpg')

cv.imshow('Image', img)
b,g,r = cv.split(img)

# cv.imshow('g',g)

# cv.imshow('r',r)

# cv.imshow('b',b)

blank = np.zeros(img.shape[:2], dtype='uint8')

bgr = cv.merge([b,g,r])

cv.imshow('BGR', bgr)

cv.waitKey(0)