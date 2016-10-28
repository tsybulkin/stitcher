#
# finding relative rotation and translation of cameras
# of two images given the list of corresponding points in both images
# 
import numpy as np


def get_fundamental_matrix(img_points):
	"""img_points - the list of tuples (uv1,uv2)
		uv1 and uv2 are the coresponding points in two images
	"""
	A = np.vstack([ np.array([u1*u2,u1*v2,u1,v1*u2,v1*v2,v1,u2,v2,1]) 
		for ((u1,v1),(u2,v2)) in img_points ])
	U,S,V = np.linalg.svd(A)
	print "singular values:",S
	h = V[8]
	return np.vstack([h[:3],h[3:6],h[6:]])
	