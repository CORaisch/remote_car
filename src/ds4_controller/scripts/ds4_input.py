#!/usr/bin/env python3

import rospy
import threading
from sensor_msgs.msg import Joy
from keyboard_controller.msg import ctrl_cmd

ds4_msg = Joy()
ds4_msg.axes = [0.0]*14 # init each of the 14 axes with 0
ds4_msg.buttons = [0]*14 # init each of the 14 buttons with 0

def callback(data):
    # update global joy message that it can be published in main loop
    # so far only those buttons are updated that are really needed
    ds4_msg.axes[0] = data.axes[0]
    ds4_msg.axes[3] = data.axes[3]
    ds4_msg.axes[4] = data.axes[4]
    ds4_msg.buttons[0] = data.buttons[0]
    ds4_msg.buttons[1] = data.buttons[1]
    ds4_msg.buttons[2] = data.buttons[2]
    ds4_msg.buttons[3] = data.buttons[3]
    ds4_msg.buttons[9] = data.buttons[9]

def main_loop():
    # main loop
    running = True
    while (not rospy.is_shutdown()) and running:
        # clear messages
        msg = ctrl_cmd()
        msg.throttle = 0.0
        msg.steer = 0.0

        # compose /ctrl_cmd messge
        msg.steer = -ds4_msg.axes[0]
        # shift throttle signal correctly to work well with car_controller
        brake = 1.0 - ((ds4_msg.axes[3]+1.0)/2.0)
        if brake > 1e-8:
            msg.throttle = -brake
        else:
            msg.throttle = 1.0 - ((ds4_msg.axes[4]+1.0)/2.0)

        # exit loop on START
        if ds4_msg.buttons[9]:
            # reset ctrl_msg and exit main loop
            print("exit on START")
            msg.throttle = 0.0
            msg.steer = 0.0
            running = False

        # publish ctrl_cmd
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

def listener():
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    # init publisher
    pub = rospy.Publisher("ctrl_cmd", ctrl_cmd, queue_size=10)
    rospy.init_node("ds4_input", anonymous=True)
    rate = rospy.Rate(60)

    # start listening on /joy message in a thread
    listener_thread = threading.Thread(target=listener)
    listener_thread.start()
    # start main loop
    main_loop()
    rospy.signal_shutdown('Quit')
