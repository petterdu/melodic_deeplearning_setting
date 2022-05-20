#!/usr/bin/env python
# -*- coding: utf-8 -*-


from turtle import delay
import turtle
import actionlib
from actionlib_msgs.msg import *
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult
from std_msgs.msg import Int16

from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist



import sys
import rospy
import math
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose
import tf
from std_msgs.msg import String, Int16, Float32
import os


moveit_commander.roscpp_initialize(sys.argv)        

group = [moveit_commander.MoveGroupCommander("ur5_manipulator")]
pose_goal = Pose()


class TestMove():

    def __init__(self):
        
        self.scene = moveit_commander.PlanningSceneInterface()
        self.robot_cmd = moveit_commander.RobotCommander()

        #robot_gripper = Mo
        self.robot_arm = group[0]
        self.robot_arm.set_goal_orientation_tolerance(0.005)
        self.robot_arm.set_planning_time(5)
        self.robot_arm.set_num_planning_attempts(5)

        rospy.sleep(2)
        # Allow replanning to increase the odds of a solution
        self.robot_arm.allow_replanning(True)        

    def move_code(self):
        global tm_count

        # #planning 1
        self.robot_arm.set_named_target("front_view")  # moveit setup assistant에서 설정한 동작
        self.robot_arm.go(wait=True)
        print("====== move plan go to front_view ======")        
        rospy.sleep(1)

    def move_code2(self):
        global tm_count

        # #planning 1
        self.robot_arm.set_named_target("button_view")  # moveit setup assistant에서 설정한 동작
        self.robot_arm.go(wait=True)
        print("====== move plan go to button_view ======")        
        rospy.sleep(1)





def newOdom (msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

def move_go(Int16):
    global state
    state = Int16.data

    if state == 1:
        print("AR no, Turn")
    if state == 0:
        print("AR find!!")

def rotation():
    global state
    global x, y, theta
    if state == 1:
        while x < 2.6:
            print(x)
            speed.linear.x = 0.3
            pub.publish(speed)
            
        while theta >-1.6:
            speed.linear.x = 0.0
            speed.angular.z = -0.3
            pub.publish(speed)
            print(theta)
        
        while y >-0.07:
            speed.linear.x = 0.1
            speed.angular.z = 0.0
            pub.publish(speed)
            print(y)
        pub2.publish(1)

        state = state +1
        tm.move_code2()

        

if __name__=='__main__':  


    rospy.init_node('send_client_goal2')
    sub = rospy.Subscriber("/odometry/filtered", Odometry, newOdom)
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    pub2 = rospy.Publisher("/talk_class", Int16, queue_size=1)
    speed = Twist()
    state = 0
    state_count =0
    x=0
    y=0
    i=0
    r = rospy.Rate(4)

    sub1 = rospy.Subscriber('/state', Int16, move_go)
    tm = TestMove()
    tm.__init__()
    tm.move_code()
    while not rospy.is_shutdown():
        rotation()