#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
from matplotlib import pyplot as plt


def talker():
    pub = rospy.Publisher('opencv', String, queue_size=10)				
    rospy.init_node('opencv_color', anonymous=True)
    rate = rospy.Rate(10)	
    while not rospy.is_shutdown():
	    _, frame = cap.read()
	    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	   
          red_lower = np.array([161, 155, 84])
	    red_higher = np.array([179, 255, 255])

	    green_lower = np.array([72,52,72])
	    green_higher = np.array([102,255,255])

	    yellow_lower = np.array([25, 146, 190])
	    yellow_higher = np.array([62, 174, 250])


	    blue_lower = np.array([100, 60, 60])
	    blue_higher = np.array([140, 255, 255])

	    white_lower = np.array([0,0,0])
	    white_higher = np.array([0,0,255])

	    red_mask = cv2.inRange(hsv_frame, red_lower, red_higher)
	    green_mask = cv2.inRange(hsv_frame, green_lower, green_higher)
	    yellow_mask = cv2.inRange(hsv_frame, green_lower, yellow_higher)
	    blue_mask = cv2.inRange(hsv_frame, blue_lower, blue_higher)	    
	    white_mask = cv2.inRange(hsv_frame, white_lower, white_higher)

	    red = cv2.bitwise_and(frame, frame, mask=red_mask)
	    green = cv2.bitwise_and(frame, frame, mask=green_mask)
	    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)
	    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
	    white = cv2.bitwise_and(frame, frame, mask=white_mask)
	    
	    
	    ret, thresh1 = cv2.threshold(red_mask, 127, 255, cv2.THRESH_BINARY)
	    ret, thresh2 = cv2.threshold(green_mask, 127, 255, cv2.THRESH_BINARY)
	    ret, thresh3 = cv2.threshold(blue_mask, 127, 255, cv2.THRESH_BINARY)
	    ret, thresh4 = cv2.threshold(white_mask, 127, 255, cv2.THRESH_BINARY)
	    ret, thresh5 = cv2.threshold(yellow_mask, 127, 255, cv2.THRESH_BINARY)

	    a=cv2.countNonZero(thresh1)
	    b=cv2.countNonZero(thresh2)
	    c=cv2.countNonZero(thresh3)
	    d=cv2.countNonZero(thresh4)
	    e=cv2.countNonZero(thresh5)

	    x=max(a,b,c,d,e)
	    y={a:"red",b:"green",c:"blue",d:"white",e:"yellow"}
	    print("color detected: ")
	    z=y[x]
	    print(z)

	    #cv2.imshow("thresh1", thresh1)
	    #cv2.imshow("thresh2", thresh2)
	    #cv2.imshow("thresh3", thresh3)
	    #cv2.imshow("thresh4", thresh4)
	    #cv2.imshow("thresh5", thresh5)

	    key = cv2.waitKey(1)
	    if key == 27:
		break
	    cv2.destroyAllWindows()	

   	    pub.publish(z)			
	    rate.sleep()					

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

















