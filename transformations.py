import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

# cv.imshow('park', img)

# trnaslate
def translateImg(img, x, y):
	transMat = np.float32([[1,0,x],[0,1,y]])
	dimensions = (img.shape[1], img.shape[0])

	return cv.warpAffine(img, transMat, dimensions)

translated_img = translateImg(img,10,10)
cv.imshow('trnaslated_img', translated_img)

def rotateImage(img, angle, rotPt=None):
	(height,width) = img.shape[:2]

	if rotPt == None:
		rotPt = (width//2,height//2) # along center

	dimensions = (width,height)

	rotMat = cv.getRotationMatrix2D(rotPt, angle, 1.0)
	return cv.warpAffine(img, rotMat, dimensions)

rotated_img  = rotateImage(img,360)
cv.imshow("rotateImage", rotated_img)

flip_x = cv.flip(img, 0)
flip_y = cv.flip(img, 1)
flip_xy = cv.flip(img, -1)

cv.imshow('flip_x',flip_x)
cv.imshow('flip_y',flip_y)
cv.imshow('flip_xy',flip_xy)


cv.waitKey(0)