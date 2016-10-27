#
# finds key points in two images
#


import numpy as np
import cv2
#from matplotlib import pyplot as plt


def run():
	img1 = cv2.imread('field_photos/DJI_0415.jpg',0)
	img2 = cv2.imread('field_photos/DJI_0416.jpg',0)

	return get_matched_points(img1,img2)



def pyrDown(img,N):
	if N <= 0: return img
	else: return pyrDown(cv2.pyrDown(img),N-1)



def get_matched_points(img1,img2):
	img1 = pyrDown(img1,3)
	img2 = pyrDown(img2,3)

	orb = cv2.ORB_create()

	kp1 = orb.detect(img1,None)
	kp1, des1 = orb.compute(img1, kp1)
	kp2 = orb.detect(img2,None)
	kp2, des2 = orb.compute(img2, kp2)

	# create BFMatcher object
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	# Match descriptors.
	matches = bf.match(des1,des2)

	# Sort them in the order of their distance.
	matches = sorted(matches, key = lambda x:x.distance)

	# Draw first 10 matches.
	img3 = img1.copy()
	img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], img3,flags=2)

	cv2.imshow('matches',img3)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == "__main__":
	run()

