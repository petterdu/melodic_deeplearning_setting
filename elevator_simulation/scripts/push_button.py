#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import math
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose
import tf
from std_msgs.msg import String, Int16, Float32, Float32MultiArray
import os


moveit_commander.roscpp_initialize(sys.argv)        
rospy.init_node('push_button',anonymous=True)

group = [moveit_commander.MoveGroupCommander("ur5_manipulator",wait_for_servers=60)]
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

    def create_wall(self):
        self.scene.remove_world_object("wall")    
        rospy.sleep(1)  
        
        button_width = (max_point_y_max+trans1[1])-(max_point_y_min+trans1[1])
        
        # create a pose
        p = PoseStamped()
        p.header.frame_id = "base_link" #robot.get_planning_frame()
        p.pose.position.x = max_point_x + trans1[0]+0.05
        p.pose.position.y = (max_point_y_max+trans1[1])+(max_point_y_min+trans1[1])/2
        p.pose.position.z = (max_point_z+trans1[2])/2
        p.pose.orientation.x = 0
        p.pose.orientation.y = 0
        p.pose.orientation.z = 0
        p.pose.orientation.w = 1

        button_width = (max_point_y_max+trans1[1])-(max_point_y_min+trans1[1])
        print(button_width)
        if button_width <0.1:
            button_width =0.3
        
        # add a box there
        self.scene.add_box("wall", p, (0.1, button_width, max_point_z+trans1[2]))
  


    def move_code(self):
        global tm_count

        # #planning 1


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
        print("====== finish push button ======") 
        tm_count =0
        group[0].set_pose_target(robot_state)
        group[0].go(wait=True)
        print("====== move plan go to front_view ======")        
        rospy.sleep(1)



def move_variable(msg):
    global move_x, move_y, move_z, count, trans1
    (trans1,rot1) = listener.lookupTransform('/base_link', '/g_camera_link', rospy.Time(0))
    # g_close = 'rostopic pub -1 /rh_p12_rn_position/command std_msgs/Float64 1.1'
    # os.system(g_close)
    move_x=msg.position.x + trans1[0] -0.19 #griper Length
    move_y=msg.position.y  +trans1[1] +0.02 #error Length
    move_z=msg.position.z  +trans1[2]

    # if move_x < 1.0:
    #     if move_x >0.7:
    #         move_x =0.7

    if move_x !=0 and move_y!=0:
        count = 1

def wall(Float32MultiArray):
    global max_point_x, max_point_y_min, max_point_y_max, max_point_z
    max_point_x = Float32MultiArray.data[0]
    max_point_y_min= Float32MultiArray.data[1]
    max_point_y_max= Float32MultiArray.data[2]
    max_point_z= Float32MultiArray.data[3]
    # print(max_point_z)
    # print(Float32MultiArray.data)

if __name__=='__main__':
    move_x=0
    move_y=0
    move_z=0
    move_x_2=0
    move_y_2=0
    move_z_2=0
    tm_count=0
    max_point_x=0
    max_point_y_min=0
    max_point_y_max=0
    max_point_z=0

    count =0
    sub = rospy.Subscriber("/endeffect_Instruction",Pose,move_variable)
    sub2 = rospy.Subscriber('/point_dict', Float32MultiArray, wall)
    pub2 = rospy.Publisher("/testtest",Int16,queue_size=10)



    
    

    while not rospy.is_shutdown():
        if count ==1:

            tm = TestMove()
            tm.__init__()
            tm.create_wall()
            tm.move_code()
            count = count +1
            rospy.sleep(0.1)
            


        
    moveit_commander.roscpp_shutdown()