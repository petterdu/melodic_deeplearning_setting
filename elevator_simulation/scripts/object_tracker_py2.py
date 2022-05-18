#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import tf
import sys
import os
import pyrealsense2 as rs
from tf import transformations as ts
from sensor_msgs.msg import Image, CameraInfo
from darknet_ros_msgs.msg import BoundingBoxes
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Transform, Vector3, Quaternion, TransformStamped
from std_msgs.msg import Header
from std_msgs.msg import String, Int16
from geometry_msgs.msg import Pose
import math
import numpy as np


msg = Pose()

class ImageListener:
    def __init__(self, topic1, topic2, topic3,topic4):
        self.topic1 = topic1
        self.topic2 = topic2
        self.topic3 = topic3
        self.bridge = CvBridge()

        self.sub = rospy.Subscriber(topic1, Image, self.imageDepthRead)
        self.sub2 = rospy.Subscriber(topic2, BoundingBoxes, self.ObjectTracking)
        self.sub_info = rospy.Subscriber(topic3, CameraInfo, self.imageDepthInfoCallback)
        self.sub3 = rospy.Subscriber(topic4, String, self.SelectClass)

        self.intrinsics = None

    def imageDepthRead(self, data_image):

        global cv_image

        try:
            cv_image = self.bridge.imgmsg_to_cv2(data_image, data_image.encoding)
            pix = (data_image.width, data_image.height)
        except CvBridgeError as e:
            print(e)
            return

    def imageDepthInfoCallback(self, cameraInfo):
        try:
            if self.intrinsics:
                return
            self.intrinsics = rs.intrinsics()
            self.intrinsics.width = cameraInfo.width
            self.intrinsics.height = cameraInfo.height
            self.intrinsics.ppx = cameraInfo.K[2]
            self.intrinsics.ppy = cameraInfo.K[5]
            self.intrinsics.fx = cameraInfo.K[0]
            self.intrinsics.fy = cameraInfo.K[4]
            self.intrinsics.model = rs.distortion.none
            self.intrinsics.coeffs = [i for i in cameraInfo.D]
        except CvBridgeError as e:
            print(e)
            return

    def ObjectTracking(self, data_BoundingBoxes):
        global cx
        global cy
        global count
        # print(data_BoundingBoxes)
        category = []

        br = tf.TransformBroadcaster()
        listener = tf.TransformListener()
        rate = rospy.Rate(10.0)
        
        # print('-------------------------------------------------------------------------------')
        for box in data_BoundingBoxes.bounding_boxes:
            if box.probability > 0.5:
                object_count = 0
                object_name = box.Class
                
                cx = (box.xmax + box.xmin)/2
                cy = (box.ymax + box.ymin)/2
                distance_in_mm = cv_image[cy, cx]
                distance_in_cm = (distance_in_mm / 10.0)
                distance_in_m = (distance_in_mm / 1000.0)
                print(distance_in_mm)
                category.append(object_name)
                for name_check_index in range(len(category)):
                    if category[name_check_index] in object_name:
                        object_count = object_count + 1

                # print('Depth at Object(%s) center(%d, %d): %f(cm)\r' % (object_name + str(object_count), cx, cy, distance_in_cm*1000))

                point = rs.rs2_deproject_pixel_to_point(self.intrinsics, [cx, cy], distance_in_m)

                trans = Transform(translation=Vector3(point[2], -point[0], -point[1]),
                            rotation=Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))
                            )

                if  box.Class ==Class_Name:                           
                    msg.position.x=(point[2])
                    msg.position.y=(-point[0])
                    msg.position.z=(-point[1])
                    if count ==1:
                        pub.publish(msg)
                        count = count +1
                    rospy.sleep(0.1)
                    
                header = Header()
                header.stamp = rospy.Time.now()
                header.frame_id = 'g_camera_link'   # the parent link

                if np.isnan(point[2])!=True:
                    trans_stamp = TransformStamped(header, object_name + str(object_count), trans)
                    br.sendTransformMessage(trans_stamp)
                

    def SelectClass(self, String):
        global Class_Name, count
        Class_Name =String.data
        if Class_Name =='올':
            Class_Name = '('
        elif Class_Name =='아':
            Class_Name = ')'
        count = 1
        print(Class_Name)
        


if __name__ == '__main__':
    rospy.init_node("object_tracker")
    
    topic1 = '/g_camera/aligned_depth_to_color/image_raw'
    # topic1 = '/g_d435/depth/g_image_raw'
    # topic2 = '/darknet_ros/bounding_boxes'
    topic2 = '/deep_pakage/boundingboxes'   
    
    
    
    pub = rospy.Publisher('/endeffect_Instruction', Pose, queue_size=10) 
    
    topic3 = '/g_camera/aligned_depth_to_color/camera_info'

    # topic3 = '/g_d435/depth/camera_info'
    topic4 = '/Class_Name'


    cv_image = 0
    cx = 0
    cy = 0
    Class_Name = "Not_Class"
    count =0

    listener = ImageListener(topic1, topic2, topic3, topic4)
    rospy.spin()
