#
# finds key points in two images
#

#import numpy as np
import cv2
#from matplotlib import pyplot as plt
	


def pyrDown(img,N):
	if N <= 0: return img
	else: return pyrDown(cv2.pyrDown(img),N-1)



def get_matched_points(photo1,photo2):
	img1 = cv2.imread(photo1,0)
	img2 = cv2.imread(photo2,0)

	img1 = pyrDown(img1,2)
	img2 = pyrDown(img2,2)

	orb = cv2.ORB_create()

	kp1 = orb.detect(img1,None)
	kp1, des1 = orb.compute(img1, kp1)
	kp2 = orb.detect(img2,None)
	kp2, des2 = orb.compute(img2, kp2)

	# create BFMatcher object
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	# Match descriptors
	matches = bf.match(des1,des2)

	# Sort them in the order of their distance.
	matches = sorted(matches, key = lambda x:x.distance)
	if len(matches) > 15: matches = matches[:15]
	
	# Select (uv1,uv2) from matched points
	points = []
	print "\n", photo1,photo2
	for m in matches:
		j,i = m.imgIdx,m.queryIdx
		#p1 = np.array(kp1[i].pt)
		#p2 = np.array(kp2[j].pt)
		points.append((kp1[i].pt,kp2[j].pt))
	return points
	
	"""
	# Draw first matches.
	img3 = img1.copy()
	img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches, img3,flags=2)

	cv2.imshow('matches',img3)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	"""


