#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
import math
yaw=0

def imu(pose):
    global yaw
    quaternion = (pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w)

    euler = euler_from_quaternion(quaternion)
    yaw= math.degrees(euler[2])
    print(yaw)

def yaw():
    rospy.init_node('bot_yaw', anonymous=True,disable_signals= True) 
    rospy.Subscriber("imu_data", Imu, imu)

    rate = rospy.Rate(10) # 10hz

    rospy.spin()

if __name__ == '__main__':
    yaw()
