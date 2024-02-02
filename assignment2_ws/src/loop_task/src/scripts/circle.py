#!/usr/bin/env python3
import math
import rospy
from geometry_msgs.msg import Twist
def circle():
    # Starts a new node
    rospy.init_node('loopy_robot', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    while not rospy.is_shutdown():
        vel_msg.linear.x = 0.2
        #Since we are moving just in x-axis
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0.2
        velocity_publisher.publish(vel_msg)
    

if __name__ == '__main__':
    try:
        #Testing our function
        circle()
    except rospy.ROSInterruptException: pass