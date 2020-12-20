#!/usr/bin/env python3

########################################################################################################
# NOTE this project is an experiment to find out how to read keyboard inputs with python.              #
#      For the final keyboard_handler, the control interface of the RC car must be investigatet first. #
########################################################################################################

import rospy
from pynput.keyboard import Key, Listener
from std_msgs.msg import String

# globals
current_msg = "neutral"

# define key press event callback
def on_press(key):
    global current_msg
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    current_msg = k

# define key release event callback
def on_release(key):
    global current_msg
    current_msg = "neutral"
    # stop on PAUSE
    if key == Key.pause:
        print("quit on PAUSE")
        return False


# main section
if __name__ == "__main__":
    # setup ros publisher
    pub = rospy.Publisher('ctrl_cmd', String, queue_size=10) # name of topic: /ctrl_cmd
    rospy.init_node('keyboard_input', anonymous=True) # name of node: /keyboard_input
    rate = rospy.Rate(10) # publish messages at 10Hz

    # setup keyboard listener
    listener = Listener(on_press=on_press, on_release=on_release, suppress=False)
    listener.start()

    # MAIN LOOP
    # endlessly react on keyboard events and send appropriate messages
    while listener.running and not rospy.is_shutdown():
        rospy.loginfo(current_msg)
        pub.publish(current_msg)
        rate.sleep()

