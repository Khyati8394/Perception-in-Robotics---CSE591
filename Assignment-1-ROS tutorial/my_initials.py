#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

speed = 1
isForward = 0

PI=3.1415926535897
speed1 = 30 
clockwise = 0

#Converting from angles to radians
angular_speed = speed1*2*PI/360

# Starts a new node
rospy.init_node('robot_cleaner', anonymous=True)
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()

vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0
    
def move(distance):
	
	print("Let's move your robot")
	#Since we are moving just in x-axis
	vel_msg.linear.x = speed

	#Setting the current time for distance calculus
	t0 = rospy.Time.now().to_sec()
	current_distance = 0 
  		   
	#Loop to move the turtle in an specified distance
	while(current_distance < distance):
		
		#Publish the velocity
		velocity_publisher.publish(vel_msg)
		#Takes actual time to velocity calculus
		t1=rospy.Time.now().to_sec()
		#Calculates distancePoseStamped
		current_distance= speed*(t1-t0)
		
	#After the loop, stops the robot
	vel_msg.linear.x = 0

def rotate(relative_angle):

	print("Let's rotate your robot")

	#We wont use linear components
	vel_msg.angular.z = angular_speed

	# Setting the current time for distance calculus
	t0 = rospy.Time.now().to_sec()
	current_angle = 0

	while(current_angle < relative_angle):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_angle = angular_speed*(t1-t0)

	#Forcing our robot to stop
	vel_msg.angular.z = 0

   
if __name__ == '__main__':
	try:
		#Testing our function
		
		rotate(97*2*PI/360)  #relative_angle = angle*2*PI/360
		move(4)
		rotate(225*2*PI/360) #relative_angle = angle*2*PI/360
		move(2)
		rotate(90*2*PI/360)  #relative_angle = angle*2*PI/360
		move(2)
		rotate(225*2*PI/360) #relative_angle = angle*2*PI/360
		move(4)

	except rospy.ROSInterruptException: pass

