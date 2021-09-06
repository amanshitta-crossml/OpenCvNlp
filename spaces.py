import cv2 as cv


img = cv.imread('Photos/park.jpg')
cv.imshow('Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

cv.waitKey(0)