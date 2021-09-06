import cv2 as cv
import numpy as np

blank = np.zeros((200,200,3), dtype='uint8')

blank[:] = 0,0,0
# blank = cv.cvtColor(blank, cv.COLOR_BGR2GRAY)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]),(255,0,0),  thickness=cv.FILLED)
cv.circle(blank, (100,100), 90, (255,255,255), thickness=-1)
cv.line(blank, (10,100),(100,100),(0,0,0), thickness=1)
cv.putText(blank, 'Hello World !', (5,100), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0), thickness=1)
cv.imshow('blank',blank)

cv.waitKey(0) 