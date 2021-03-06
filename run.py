# 
# this module runs the entire process of
# detecting key points, matching them, finding relative R and T and so on
#
import os
from point_detect import get_matched_points
from cam_position import get_fundamental_matrix



my_path = 'field_photos/'
photos = [ f for f in os.listdir(my_path) if f[-3:]=='JPG' or f[-3:]=='jpg' ]
print "found photos:",photos

points = [ get_matched_points(my_path+photos[i],my_path+photos[i+1]) 
	for i in range(len(photos)-1) ]

F = get_fundamental_matrix(points[0])
print F