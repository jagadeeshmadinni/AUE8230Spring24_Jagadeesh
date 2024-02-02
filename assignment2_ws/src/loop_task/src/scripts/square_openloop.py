#!/usr/bin/env python3
import math
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def move():
    # Starts a new node
    rospy.init_node('loopy_robot', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose)
    vel_msg = Twist()


    linear_speed = 0.2
    distance = 2
    angular_speed = 0.2
    rotation = math.pi/2
    

    while not rospy.is_shutdown():

        for itr in range(4):
            vel_msg.linear.x = linear_speed
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            #Setting the current time for distance calculus
            t0 = rospy.Time.now().to_sec()
            current_distance = 0



            #Loop to move the turtle in an specified distance
            while(current_distance < distance):
                #Publish the velocity
                velocity_publisher.publish(vel_msg)
                #Takes actual time to velocity calculus
                t1=rospy.Time.now().to_sec()
                #Calculates distancePoseStamped
                current_distance= linear_speed*(t1-t0)
            #After the loop, stops the robot
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            #Force the robot to stop
            velocity_publisher.publish(vel_msg)

            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = angular_speed

            t0 = rospy.Time.now().to_sec()
            current_angle = 0

            while(current_angle < rotation):
                velocity_publisher.publish(vel_msg)
                t1 = rospy.Time.now().to_sec()
                current_angle = angular_speed*(t1-t0)
                        #After the loop, stops the robot

            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            #Force the robot to stop
            velocity_publisher.publish(vel_msg)





if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass