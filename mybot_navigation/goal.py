#!/usr/bin/env python

import rospy
import geonav_conversions as gc
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Point, PointStamped
import sys
import tf

def movebase_client():
    
    lat=float(sys.argv[1])
    lon=float(sys.argv[2])
    utm = gc.fromLatLong(lat,lon)
    utm1 = gc.UTMPoint.toPoint(utm)
    utm2 = PointStamped()
    utm2.header.frame_id= "utm"
    utm2.point = utm1
    
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

    # Getting transform from utm to odom frame
    listener = tf.TransformListener()
    listener.waitForTransform("utm", "odom", rospy.Time(0),rospy.Duration(4.0))
    odom = listener.transformPoint("odom", utm2)
    

    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "odom"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = odom.point.x
    goal.target_pose.pose.position.y = odom.point.y
    goal.target_pose.pose.orientation.w = 1.0
    #goal.target_pose.pose.position.y = utmy

    # Sends the goal to the action server.
    client.send_goal(goal)
    # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
    # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        # Result of executing the action
        return client.get_result()

if __name__ == '__main__':
    try:
        # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
