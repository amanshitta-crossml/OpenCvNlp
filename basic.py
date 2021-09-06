import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)


# convert to GRAYSCALE
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscaled',gray_img)

# BLUR ON IMAGE
blur = cv.GaussianBlur(gray_img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blurred',blur)


# Edge Cascade
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny', canny)

# Dilating edges 
dilated_img = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('dilated_img', dilated_img)

# Eroding images
erode = cv.erode(dilated_img, (3,3), iterations=3)
cv.imshow('erode',erode)

# Resize
resized = cv.resize(img,(250,250))
cv.imshow('Resized',resized)

# Cropping
crop = img[10:200,100:200]
cv.imshow('crop',crop)

cv.waitKey(0)