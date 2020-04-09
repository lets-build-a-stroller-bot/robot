#!/usr/bin/python2

#future imports
from __future__ import print_function

#ros imports
import rospy
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState

#std imports
from threading import Thread
import sys
from pynput import keyboard


#establish ros node and publisher to velocity
rospy.init_node("teleop_robot")
vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

LIN_SPEED = 0.1
ANG_SPEED = 1

vel_msg = Twist()
key_state = {}

def repositionBot():
    state_msg = ModelState()
    state_msg.model_name = 'turtlebot3_burger'
    state_msg.pose.position.x = 0
    state_msg.pose.position.y = -1.75
    rospy.wait_for_service('/gazebo/set_model_state')
    set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
    set_state(state_msg)
    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    return vel_msg
    

def key_update(key, state):

    #key is pressed for the first time
    if key not in key_state:
        key_state[key] = state
        return True

    # key changed state
    if state != key_state[key]:
        key_state[key] = state
        return True

    #no change
    return False



stop_display = False
def key_press(key):
    if key == keyboard.Key.esc:
        global stop_display
        stop_display = True
        print('\nPress Ctrl+C to exit')
        return False
    try:
        #character input
        k = key.char
    except:
        #arrow key/other input
        k = key.name


    #check if press changes state0.1
    change = key_update(key, True)
    if change:
        global vel_msg, LIN_SPEED, ANG_SPEED
        if   k in ['w', 'up']:
            vel_msg.linear.x += LIN_SPEED
        elif k in ['s', 'down']:
            vel_msg.linear.x -= LIN_SPEED
        elif k in ['d', 'right']:
            vel_msg.angular.z -= ANG_SPEED
        elif k in ['a', 'left']:
            vel_msg.angular.z += ANG_SPEED
        elif k in ['c']:
            ANG_SPEED += .1
            print(ANG_SPEED)
        elif k in ['v']:
            ANG_SPEED += .1
            print(ANG_SPEED)
        elif k in ['z']:
            LIN_SPEED += .1
            print(LIN_SPEED)
        elif k in ['x']:
            LIN_SPEED -= .1
            print(LIN_SPEED)
        elif k in ['r']:
            repositionBot()
    return True
    

def key_release(key):
    try:
        #character input
        k = key.char
    except:
        #arrow key/other input
        k = key.name

    change = key_update(key, False)
    if change:
        global vel_msg
        if   k in ['w', 'up']:
            vel_msg.linear.x = 0
        elif k in ['s', 'down']:
            vel_msg.linear.x = 0
        elif k in ['d', 'right']:
            vel_msg.angular.z = 0
        elif k in ['a', 'left']:
            vel_msg.angular.z = 0

    return True
    

rate = rospy.Rate(10)
def user_display():
    print('Use WSAD or the ARROW KEYS to control.\nUse c/v to increase turn speed.\nUse x/z to increase/decrease speed.\nUse R to reset robot')
    while True:
        try:
            print('\r' + ' '*80,end='')
            sys.stdout.flush()
            log_str = "\r\t\tX: {}\tTHETA: {}\t".format(vel_msg.linear.x,
                                                          vel_msg.angular.z)
            print(log_str, end=' ')
            sys.stdout.flush()

            global stop_display
            if stop_display:
                exit(0) 

            if not rospy.is_shutdown():
                rate.sleep()
                vel_pub.publish(vel_msg)
            else:
                exit(0)
        except KeyboardInterrupt:
            exit(0)


#start key listener thread
key_listener = keyboard.Listener(on_press=key_press, on_release=key_release) 
key_listener.start()

#start user display thread
display_thread = Thread(target=user_display)
display_thread.start()

#update ros topics on main thread
rospy.spin()

