#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import math
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose
import tf
from std_msgs.msg import String, Int16, Float32
import os


moveit_commander.roscpp_initialize(sys.argv)        
rospy.init_node('push_button',anonymous=True)

group = [moveit_commander.MoveGroupCommander("ur3_manipulator",wait_for_servers=15)]
pose_goal = Pose()
listener = tf.TransformListener()
listener2 = tf.TransformListener()


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
        # self.robot_arm.set_named_target("front_view")  # moveit setup assistant에서 설정한 동작
        # self.robot_arm.go(wait=True)
        # print("====== move plan go to front_view ======")        
        # rospy.sleep(1)

        #robot state print
        robot_state = self.robot_arm.get_current_pose()
        robot_angle = self.robot_arm.get_current_joint_values()
        print(robot_state)

        #planning 2
        pose_goal.orientation.x = 0.707
        pose_goal.orientation.y = 0.0
        pose_goal.orientation.z = 0.707
        pose_goal.orientation.w = 0.0

        pose_goal.position.x = move_x # red line      0.2   0.2
        pose_goal.position.y = move_y  # green line  0.15   0.15
        pose_goal.position.z = move_z  # blue line   # 0.35   0.6
        group[0].set_pose_target(pose_goal)
        group[0].go(wait=True)
        # active_push(0)
        # rospy.sleep(5)
        tm_count =0
        # pub.publish(1)

    def move_code2(self):

        # #planning 1
        # self.robot_arm.set_named_target("front_view")  # moveit setup assistant에서 설정한 동작
        # self.robot_arm.go(wait=True)
        # print("====== move plan go to front_view ======")        
        # rospy.sleep(1)

        #robot state print
        robot_state = self.robot_arm.get_current_pose()
        robot_angle = self.robot_arm.get_current_joint_values()
        print(robot_state)

        #planning 2
        pose_goal.orientation.x = 0.707
        pose_goal.orientation.y = 0.0
        pose_goal.orientation.z = 0.707
        pose_goal.orientation.w = 0.0

        pose_goal.position.x = move_x_2 # red line      0.2   0.2
        pose_goal.position.y = move_y_2  # green line  0.15   0.15
        pose_goal.position.z = move_z_2  # blue line   # 0.35   0.6
        group[0].set_pose_target(pose_goal)
        group[0].go(True)

def move_variable(msg):
    global move_x, move_y, move_z, count
    (trans1,rot1) = listener.lookupTransform('/base_link', '/g_camera_link', rospy.Time(0))
    g_close = 'rostopic pub -1 /rh_p12_rn_position/command std_msgs/Float64 1.1'
    os.system(g_close)
    move_x=msg.position.x + trans1[0] -0.185 #griper Length
    move_y=msg.position.y  +trans1[1] #error Length
    move_z=msg.position.z  +trans1[2]

    # if move_x < 1.0:
    #     if move_x >0.7:
    #         move_x =0.7

    if move_x !=0 and move_y!=0:
        count = 1

# def active_push(count):
#     global tm_count, move_x_2, move_y_2, move_z_2
#     tm_count = count
#     if tm_count ==0:
#         pub2.publish(1)
#         tm = TestMove()
#         tm.__init__()
#         listener.waitForTransform("/base_link", "/ee_link", rospy.Time(), rospy.Duration(4.0))
#         (trans3,rot1) = listener2.lookupTransform('/base_link', '/ee_link', rospy.Time(0))
#         move_x_2=trans3[0]+ 0.1
#         move_y_2=trans3[1]
#         move_z_2=trans3[2]
#         tm.move_code2()
#         tm_count = tm_count+1

def active_push(Float32):
    global tm_count, move_x_2, move_y_2, move_z_2
    if tm_count ==0:
        g_close = 'rostopic pub -1 /rh_p12_rn_position/command std_msgs/Float64 1.1'
        pub2.publish(1)
        tm = TestMove()
        tm.__init__()
        listener.waitForTransform("/base_link", "/ee_link", rospy.Time(), rospy.Duration(4.0))
        (trans3,rot1) = listener2.lookupTransform('/base_link', '/ee_link', rospy.Time(0))
        nan_Check = float(Float32.data)
        
        print("------------------------")
        print(math.isnan)
        if math.isnan(nan_Check)!=True:
            os.system(g_close)
            print("dist is ")
            print(Float32.data)
            move_x_2=trans3[0]+ Float32.data -0.15
            move_y_2=trans3[1]
            move_z_2=trans3[2]
            tm.move_code2()
            tm_count = tm_count+1
        else:
            os.system(g_close)
            print("dist is nan")
            move_x_2=trans3[0]+ 0.15
            move_y_2=trans3[1]
            move_z_2=trans3[2]
            tm.move_code2()
            tm_count = tm_count+1




if __name__=='__main__':
    move_x=0
    move_y=0
    move_z=0
    move_x_2=0
    move_y_2=0
    move_z_2=0
    tm_count=0

    count =0
    sub = rospy.Subscriber("/endeffect_Instruction",Pose,move_variable)
    # sub2 = rospy.Subscriber("/endeffect_push",Int16,active_push)
    # pub = rospy.Publisher("/dist_Request",Int16,queue_size=10)
    pub2 = rospy.Publisher("/testtest",Int16,queue_size=10)
    # sub3 = rospy.Subscriber("/dist_reward",Float32,active_push)


    
    

    while not rospy.is_shutdown():
        if count ==1:
            tm = TestMove()
            tm.__init__()
            tm.move_code()
            count = count +1
            rospy.sleep(0.1)
            


        
    moveit_commander.roscpp_shutdown()