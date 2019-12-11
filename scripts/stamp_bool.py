#!/usr/bin/env python

import roslib; roslib.load_manifest( 'subt_rviz_plugins' )
from std_msgs.msg import Bool
from subt_rviz_plugins.msg import BoolStamped
import rospy

topic = 'gas_detected_stamped'
publisher = rospy.Publisher(topic, BoolStamped, queue_size=5)

rospy.init_node('detector_bridge')

def onMsg(msg):
    new_msg = BoolStamped()
    new_msg.header.frame_id = '/X2/base_link'
    new_msg.header.stamp = rospy.Time.now()
    new_msg.data = msg.data
    publisher.publish(new_msg)

subscriber = rospy.Subscriber('/X2/gas_detected', Bool, onMsg)

while not rospy.is_shutdown():
    rospy.spin()

