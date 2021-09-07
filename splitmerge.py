import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Image', img)
b,g,r = cv.split(img)

cv.imshow('g',g)

cv.imshow('r',r)

cv.imshow('b',b)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)



blank = np.zeros(img.shape[:2], dtype='uint8')

# blue =  cv.merge([b,blank,blank])
# green =  cv.merge([blank,g,blank])
# red =  cv.merge([blank,blank,r])

# cv.imshow('Blue', blue)
# cv.imshow('Green', green)
# cv.imshow('Red', red)


bgr = cv.merge([b,g,r])

cv.imshow('BGR', bgr)

cv.waitKey(0)