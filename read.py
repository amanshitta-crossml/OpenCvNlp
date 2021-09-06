import cv2 as cv
import pdb


# # read and display and image
# img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)


# # read a video file frame by frame

capture = cv.VideoCapture(0)

while 1:

	isTrue, frame = capture.read()
	cv.imshow('Video-frames',frame)

	# pdb.set_trace()
	cv.imshow('Video-frames',frame)

	if cv.waitKey(20) & 0xFF == ord('d'):
		break

capture.release()
cv.destroyAllWindows()   
