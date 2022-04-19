#!/usr/bin/env python3

from pickletools import float8
import rospy
import sys
from sensor_msgs.msg import Image as msg_Image
sys.path.remove('/opt/ros/melodic/lib/python2.7/dist-packages')
sys.path.append('/home/kmw/catkin_ws/install/lib/python3/dist-packages')
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String, Int16, Float32

import os

class ImageListener:
    def __init__(self, topic):
        self.topic = topic
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber(topic, msg_Image, self.imageDepthCallback)

    def imageDepthCallback(self, data):
        global state_count
        try:
            if state_count==1:
                cv_image = self.bridge.imgmsg_to_cv2(data, data.encoding)
                pix = (data.width/2, data.height/2)
                pub.publish(cv_image[240,320])
                print(cv_image[240,320])
                print(state_count)
                rospy.sleep(0.1)
                # # sys.stdout.write('%s: Depth at center(%d, %d): %f(mm)\r' % (self.topic, pix[0], pix[1], cv_image[pix[1], pix[0]]))
                # sys.stdout.flush()
                state_count = state_count +1
        except CvBridgeError as e:
            print(e)
            return

def start_count(Int16):
    global state_count
    state_count = Int16.data


if __name__ == '__main__':
    state_count=0
    rospy.init_node("depth_image_processor")
    sub2 = rospy.Subscriber("/dist_Request",Int16,start_count)
    pub = rospy.Publisher("/dist_reward",Float32, queue_size=10)
    



    while not rospy.is_shutdown():

        topic = '/g_d435/depth/g_image_raw'  # check the depth image topic in your Gazebo environmemt and replace this with your
        listener = ImageListener(topic)
