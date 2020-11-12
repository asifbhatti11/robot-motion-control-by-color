#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

n = String()

def callback(data):
    global n
    #rospy.loginfo(data.data)
    n=str(data.data) 

if __name__=="__main__":
    global n
    rospy.init_node('turtlebot3_color')				
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)		 
    sub = rospy.Subscriber('opencv', String, callback)	
    rate = rospy.Rate(10)
    target_linear_vel   = 0.0
    target_angular_vel  = 0.0
    control_linear_vel  = 0.0
    control_angular_vel = 0.0
    try:
        while(1):
      	    print (n)
            if n=="red":				
                target_linear_vel = 0.15
	        target_angular_vel=0
	    elif n=="yellow":				
                target_linear_vel = -0.15
	        target_angular_vel=0
            elif n=="green" :
		target_angular_vel = 0.5
                target_linear_vel = 0
	    elif n=="blue" :
		target_angular_vel = -0.5
                target_linear_vel = 0
            elif n=="white":			
                target_linear_vel   = 0.0
                control_linear_vel  = 0.0
                target_angular_vel  = 0.0
                control_angular_vel = 0.0
          
            a={"red":"forward","white":"stopping","green":"right","blue":"left","yellow":"backward"}
	    b=a.get(n)
	    #print("color detected: ")
	    #print(n)
	    print("moving robot:")
	    print(b)

	    twist = Twist()
	    control_linear_vel = target_linear_vel		
	    control_angular_vel = target_angular_vel	   
            twist.linear.x = control_linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = control_angular_vel
            pub.publish(twist)
	    rate.sleep()					


    except rospy.ROSInterruptException:
        pass


