#!/usr/bin/env python
import cv2
#import pyrealsense as pyrs
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import Bool

import roslib
import rospy

bridge = CvBridge()

def callback(data):
   	
	print("got some data")
#	img = br.compressed_imgmsg_to_cv2(data)
	img = br.imgmsg_to_cv2(data)
	cv2.imwrite('messigray.bmp',img)
	cv_image =  bridge.imgmsg_to_cv2(data, "8UC3")
    	#except CvBridgeError as e:
      	#	print(e)
	cv2.imshow('frame',img)
	pub.publish(data)	
	cv2.waitKey(10)

br = CvBridge()

pub = rospy.Publisher('send_to_telegram', Image, queue_size=10)
#pub = rospy.Publisher('send_to_telegram', , queue_size=10)
rospy.Subscriber('picture', Image, callback)

rospy.init_node('get_image', anonymous=True)
rospy.spin()
