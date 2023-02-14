import math
from PIL import Image
import cv2
from detect_face import face

import rospy
from geometry_msgs.msg import Twist


def Run(robot):
    # robot.set_move_speed(1)
    # robot.go_forward(1)

    print robot.get_box_position()

    twist = Twist()
    twist.linear.x = 0
    twist.angular.z = math.radians(0)
    rate = rospy.Rate(20)
    for _ in xrange(20):
        robot.publish_twist(twist)
        rate.sleep()

    while(1):
	x = 0#int(input('x: '))
	z = 0#int(input('z: '))
	print('0, 0')
        twist = Twist()
        twist.linear.x = x
        twist.angular.z = math.radians(z)
        rate = rospy.Rate(20)
        for _ in xrange(20):
            robot.publish_twist(twist)
            rate.sleep()

	img = robot.get_image()
	face(img,1)
	print('11111111111111111111111')
	#img = Image.fromarray(img, 'RGB')
	#print('22222222222222222222222')
	#print(type(img))
	#img.save('1.png')
