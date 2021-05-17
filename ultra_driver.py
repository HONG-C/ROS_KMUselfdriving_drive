#!/usr/bin/env python
# -*- coding: utf-8 -*-

#과제 1
import rospy, math
from std_msgs.msg import Int32MultiArray


#거리센서 값 선언 및 초기화 
FL=0
FM=0
FR=0
R=0
L=0
P_VAL=0#차량의 중간점 복귀를 위한 변수 

def callback(msg):
#거리값 획득 및 변수 저장 
 	global FL
	global FM
	global FR
	global R
	global L
	FL=msg.data[0]
	FM=msg.data[1]
	FR=msg.data[2]
	R=msg.data[6]
	L=msg.data[7]
	print(msg.data)


#직선 주행 시 자세제어를 위한 함수 
def go_straight(P_VAL):
	angle = 0+P_VAL+(FR-FL)
	xycar_msg.data = [angle, 40]
	

#우회전을 위한 함수 
def turn_right():
	angle = 80
	xycar_msg.data = [angle, 40]

#좌회전을 위한 함수 
def turn_left():
	angle = -80
	xycar_msg.data = [angle, 40]

rospy.init_node('guide')
motor_pub = rospy.Publisher('xycar_motor_msg', Int32MultiArray, queue_size=1)
ultra_sub = rospy.Subscriber('ultrasonic', Int32MultiArray, callback)

xycar_msg = Int32MultiArray()


while not rospy.is_shutdown():
		P_VAL=2*(R-L)#차량 좌우 거리 확인 
		if FM>250:
			go_straight(P_VAL)
		elif FL<FR&FR>100:
			turn_right()
		elif FL>100:
			turn_left()
		else:
			angle=0
			xycar_msg.data = [angle, 40]


		motor_pub.publish(xycar_msg)



		
