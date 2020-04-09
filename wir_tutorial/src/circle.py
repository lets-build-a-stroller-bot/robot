#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState

from math import sin

def repositionBot():
    state_msg = ModelState()
    state_msg.model_name = 'turtlebot3_burger'
    state_msg.pose.position.x = 1.2
    state_msg.pose.position.y = -1.25
    rospy.wait_for_service('/gazebo/set_model_state')
    set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
    set_state(state_msg)

def main():
    rospy.init_node('circler', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
    
    repositionBot()
    
    rate = rospy.Rate(2) # 10hz
    msg = Twist()
    msg.linear.x = .2
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = .5

    while not rospy.is_shutdown():
        #msg.linear.x += .1
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
