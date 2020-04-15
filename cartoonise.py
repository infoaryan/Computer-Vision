import cv2
import numpy


#Initiating the camera
cap= cv2.VideoCapture(0)

#Infinite loop for capturing the frames
while(True):
	_,image1 = cap.read()

	image = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
	image = cv2.medianBlur(image,3)
	
	#Getting the edges of the image
	edges1 = cv2.Laplacian(image, -1,ksize=5)
	_,mask = cv2.threshold(edges1,50, 255, cv2.THRESH_BINARY_INV)
	for i in range(2):
		mask= cv2.medianBlur(mask,3)

	kernel = numpy.ones((3,3),numpy.uint8)
	mask = cv2.erode(mask, kernel)
	
	image_b, image_g, image_r = cv2.split(image1)

	final_b = cv2.bitwise_and(image_b, mask)
	final_g = cv2.bitwise_and(image_g, mask)
	final_r = cv2.bitwise_and(image_r, mask)

	final = cv2.merge((final_b,final_g,final_r))

	cv2.imshow('cartoon',final)
	if(cv2.waitKey(3)==ord('q')):
		break

cap.release()
writer.release()
cv2.destroyAllWindows()
