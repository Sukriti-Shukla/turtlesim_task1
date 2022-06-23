#!/usr/bin/env python
# import necesary modules
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import *
from std_srvs.srv import Empty
from math import pow, atan2, sqrt, sin, cos, tan
from cmath import pi
import time


class turtle1:
    def __init__(self):
        rospy.init_node('turtle1', anonymous=True)
        self.velocity_publisher = rospy.Publisher(
            '/turtle1/cmd_vel', Twist, queue_size=10)
        self.velocity_subscriber = rospy.Subscriber(
            '/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(100)
        # vx = input('Enter vx velocity of turtle1')
        # vy = input('Enter vy velocity of turtle1')

    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def move(self):
        v_msg = Twist()
        v_msg.linear.x = 4
        v_msg.linear.y = 2
        time.sleep(1)
        self.velocity_publisher.publish(v_msg)
        while not rospy.is_shutdown():
            print(v_msg.linear.x, v_msg.linear.y, self.pose.x, self.pose.y)
            if (self.pose.x < 1) or (self.pose.x > 10):
                if (self.pose.x > 10) and v_msg.linear.x > 0:
                    v_msg.linear.x = -1*v_msg.linear.x
                if (self.pose.x < 1) and v_msg.linear.x < 0:
                    v_msg.linear.x = -1*v_msg.linear.x

            if (self.pose.y < 1) or (self.pose.y > 10):
                if (self.pose.y > 10) and v_msg.linear.y > 0:
                    v_msg.linear.y = -1*v_msg.linear.y
                if (self.pose.y < 1) and v_msg.linear.y < 0:
                    v_msg.linear.y = -1*v_msg.linear.y
            self.velocity_publisher.publish(v_msg)

        # Publish at the desired rate.
        self.rate.sleep()


if __name__ == '__main__':
    try:
        x = turtle1()
        x.move()
    except rospy.ROSInterruptException:
        pass
