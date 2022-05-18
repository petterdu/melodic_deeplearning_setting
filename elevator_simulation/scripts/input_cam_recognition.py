#!/usr/bin/env python3

from __future__ import print_function
import rospy


import roslib
roslib.load_manifest('deep_pakage')
from deep_pakage.msg import boundingbox, boundingboxes, objectcount
import actionlib
from deep_pakage import *

import sys
import os
from sensor_msgs.msg import Image as SensorImage
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
import tensorflow as tf
from std_msgs.msg import String, Int16

# sys.path.append('/home/kmw/catkin_ws/src/deep_pakage/msg/boundingbox.msg')

sys.path.append('/home/kmw/catkin_ws/src/elevator_buttons_recognition')
from button_recognition import ButtonRecognition
import cv2
sys.path.remove('/opt/ros/melodic/lib/python2.7/dist-packages')
sys.path.append('/home/kmw/catkin_ws/install/lib/python3/dist-packages')
from cv_bridge import CvBridge







def callback(imgmsg):

    global recognizer,bridge

    img = bridge.imgmsg_to_cv2(imgmsg, desired_encoding='passthrough')
    img2= img.copy()
    resultimg,japo=recognizer.predict(img2, True)
    japolength=len((japo))
    boxex_list=boundingboxes()
    box_list=[]
    
    if (japolength != 0):
        boxex_list.header.stamp = rospy.Time.now()
        boxex_list.header.frame_id = "detection"
        boxex_list.image_header.stamp = rospy.Time.now()
        boxex_list.image_header.frame_id = "detection"
        for i in range(japolength):
            box_info = boundingbox()
            box_info.probability = japo[i][1]
            box_info.xmin = japo[i][4][0]
            box_info.ymin = japo[i][4][1]
            box_info.xmax = japo[i][4][2]
            box_info.ymax = japo[i][4][3]
            box_info.id = 0
            box_info.Class = japo[i][2]
            box_list.insert(i,box_info)

        # for i in range(japolength):
        #     box_list.insert(i,[[japo[i][1],japo[i][4][0]],japo[i][4][1],japo[i][4][2],japo[i][4][3],0,japo[i][2]])
        # for i in range(len(box_list)):   
        #     print(box_list[i])
        for i in range(len(box_list)):
            
            boxex_list.bounding_boxes.insert(i, box_list[i])

        pub.publish(box_info)
        pub1.publish(boxex_list)






        

    
    cv2.imshow('frame',resultimg)
    cv2.waitKey(1)

def give_signal(Int16):
    global state
    state =Int16.data

def main():

    global recognizer,bridge, pub, pub1, r
    rospy.init_node('listener', anonymous=True)
    bridge = CvBridge()
    recognizer = ButtonRecognition()
    pub = rospy.Publisher('/deep_pakage/boundingbox',boundingbox, queue_size=10)
    pub1 = rospy.Publisher('/deep_pakage/boundingboxes',boundingboxes, queue_size=10)
    r = rospy.Rate(4)
    state=0
    
    # rospy.Subscriber("/usb_cam/image_raw", SensorImage, callback)
    # sub = rospy.Subscriber("/g_d435/rgb/g_image_raw", SensorImage, callback)
    sub = rospy.Subscriber("/g_camera/color/image_raw", SensorImage, callback)
    
    #rospy.Subscriber("/camera1/color/image_raw", SensorImage, callback)

    #simply keeps python from exiting until this node is stopped
    rospy.spin()    

    recognizer.clear_session()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

# end of file
