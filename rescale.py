import cv2 as cv
     
def rescaleFrame(frame, scale=.75):
	"""
	rescale a frame down or up
	can be used for image, video, live vid
	"""

	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)

	dimensions = (width, height)
	
	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
	"""
	works only for live video
	rescalse and changes video
	"""

	live_capture.set(3, width)
	live_capture.set(4, height)


live_capture = cv.VideoCapture(0)
changeRes(200,200)
while True:
	isTrue, frame  = live_capture.read()

	cv.imshow('live_res',frame)

	if cv.waitKey(0) & 0xff == ord('d'):
		break

live_capture.release()
cv.destroyAllWindows()


# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:

# 	isTrue, frame = capture.read()
# 	# rescale the video frame by frame
# 	resized_frame = rescaleFrame(frame)
	
# 	cv.imshow('unsized',frame)
# 	cv.imshow('resized',resized_frame)

# 	if cv.waitKey(0) & 0XFF == ord('d'):
# 		break

# capture.release()
# cv.destroyAllWindows()