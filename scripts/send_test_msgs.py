#!/usr/bin/env python

import roslib; roslib.load_manifest( 'subt_rviz_plugins' )
from sensor_msgs.msg import LaserScan
import rospy
from math import cos, sin
import tf

topic = 'scan'
publisher = rospy.Publisher( topic, LaserScan, queue_size=5 )

rospy.init_node( 'test_scan' )

br = tf.TransformBroadcaster()
rate = rospy.Rate(10)
radius = 5
angle = 0

dist = 3
while not rospy.is_shutdown():

    scan = LaserScan()
    scan.header.frame_id = "/base_link"
    scan.header.stamp = rospy.Time.now()

    scan.angle_min = 3.14159274101
    scan.angle_max = 3.14159274101
    scan.angle_increment = float('nan')
    scan.time_increment = 0.0
    scan.range_min = 0.04
    scan.range_max = 40.0
    scan.ranges = [10.0]
    scan.intensities = [0.0]

    publisher.publish(scan)

    br.sendTransform((radius * cos(angle), radius * sin(angle), 0),
                     tf.transformations.quaternion_from_euler(0, 0, angle),
                     rospy.Time.now(),
                     "base_link",
                     "map")
    angle += .01
    rate.sleep()

