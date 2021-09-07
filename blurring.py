import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)

# Average blur
average = cv.blur(img,(3,3),0)
cv.imshow('Average', average)

# Gaussian Blur
gaus = cv.GaussianBlur(img, (5,5), 0)
cv.imshow("Gaussian", gaus)
# Median Blur

# Bilateral (bilateralFilter)
bilateral = cv.bilateralFilter(img, 7, 55,55)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)