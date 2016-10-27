#
# finds key points in two images
#


import numpy as np
import cv2
import os
#from matplotlib import pyplot as plt


def run():
	my_path = 'field_photos/'
	photos = [ f for f in os.listdir(my_path) if f[-3:]=='JPG' or f[-3:]=='jpg' ]
	print photos

	[ get_matched_points(my_path+photos[i],my_path+photos[i+1]) for i in range(len(photos)-1) ]
	
	


def pyrDown(img,N):
	if N <= 0: return img
	else: return pyrDown(cv2.pyrDown(img),N-1)



def get_matched_points(photo1,photo2):
	img1 = cv2.imread(photo1,0)
	img2 = cv2.imread(photo2,0)

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
	print "\n", photo1,photo2
	print [ m.distance for m in matches]
	# imgIdx', 'queryIdx'
	"""
	# Draw first 10 matches.
	img3 = img1.copy()
	img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], img3,flags=2)

	cv2.imshow('matches',img3)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	"""


if __name__ == "__main__":
	run()

