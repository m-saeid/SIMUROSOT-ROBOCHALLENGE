# coding=utf-8
from math import radians
from robot import Robot




def Run(robot):
	print("we set moving speed of robot equal to 0.3 meters per second")
	robot.set_move_speed(0.3)

	print("we set turning speed of robot equal to -10 degree per second (-10 degree means turning to clockwise by 10 degree)")
	robot.set_turn_speed(-10)

	print("we go forward for 11 seconds (3.3 meters)")
	robot.go_forward(11)
	
	print("we turn for 3 seconds (30 degree clockwise)")
	robot.turn_around(3)

	print("we go forward for 2 seconds (0.6 meters)")
	robot.go_forward(2)

	print("we set turning speed of robot equal to 12 degree per second (12 degree means turning to counter-clockwise by 12 degree)")
	robot.set_turn_speed(12)
	
	print("we turn for 3 seconds (36 degree counter-clockwise)")
	robot.turn_around(3)
	
	print("we go forward for 3 seconds (0.9 meters)")
	robot.go_forward(3)

	print("we turn for 3 seconds (36 degree counter-clockwise)")
	robot.turn_around(3)

	print("we go forward for 3 seconds (0.9 meters)")
	robot.go_forward(3)
	




robot_model=Robot()

Run(robot_model)
	

	
	

	
