#!/usr/bin/env python

########################################################################################################
# NOTE this project is an experiment to find out how to read keyboard inputs with python.              #
#      For the final keyboard_handler, the control interface of the RC car must be investigatet first. #
########################################################################################################

###############################################################################################################################################
# TODO change font on the screen -> increase size, bold?                                                                                      #
# TODO write some additionla info text on the display -> "This window needs to be focussed in order to capture key commands", "Controls: ..." #
###############################################################################################################################################

import rospy
import pygame
from pygame.locals import *
from keyboard_input.msg import ctrl_cmd

# globals
bg_color    = (41, 43, 46)
text_color  = (255, 255, 255)
display_res = (640, 480)

# compose string from buffer
def str_from_buf(buf):
    if len(buf) != 0:
        str = buf[0]
        for i in range(1,len(buf)):
            str = str + " & " + buf[i]
    else:
        str = "Neutral"
    return str

# render simple display which needs to be focused in order to catch key commands
def display(str):
    # clear screen
    screen.fill(bg_color)

    # render some informational text
    text = font.render(str, True, text_color, bg_color)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    screen.blit(text, textRect)
    pygame.display.update()


# main section
def main_loop():
    # init ros communication
    pub = rospy.Publisher("ctrl_cmd", ctrl_cmd, queue_size=10) # topic name: /ctrl_cmd
    rospy.init_node("keyboard_input", anonymous=True) # node name: /keyboard_input
    rate = rospy.Rate(60) # send messages at 60Hz

    # main loop
    running = True
    while (not rospy.is_shutdown()) and running:
        # update keyboard input map
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        # clear messages
        msgs = []
        msg = ctrl_cmd()
        msg.throttle = 0.0
        msg.steer = 0.0

        # hacked event handling
        if keys[K_UP]:
            msgs.append("Accelerate")
            msg.throttle = msg.throttle + 1.0
        if keys[K_LEFT]:
            msgs.append("Steer Left")
            msg.steer = msg.steer + -1.0
        if keys[K_RIGHT]:
            msgs.append("Steer Right")
            msg.steer = msg.steer + 1.0
        if keys[K_DOWN]:
            msgs.append("Brake")
            msg.throttle = msg.throttle + -1.0
        if not keys[K_UP] and not keys[K_DOWN] and not keys[K_LEFT] and not keys[K_RIGHT]:
            msgs.append("Neutral")

        # do not allow accelerate & brake simultaneously
        if keys[K_UP] and keys[K_DOWN]:
            if "Accelerate" in msgs: msgs.remove("Accelerate")
            msg.throttle = -1.0

        # do not allow steer left & right simultaneously
        if keys[K_LEFT] and keys[K_RIGHT]:
            if "Steer Left" in msgs: msgs.remove("Steer Left")
            if "Steer Right" in msgs: msgs.remove("Steer Right")

        # quit on ESC
        if keys[K_ESCAPE]:
            msgs = ["Exit"]
            msg.throttle = 0.0
            msg.steer = 0.0
            running = False

        # render window and display some information
        msg_str = str_from_buf(msgs)
        display(msg_str)

        # publish and log ros msgs
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    # init pygame
    pygame.init()
    screen = pygame.display.set_mode(display_res)
    pygame.display.set_caption("robocar keyboard input")
    screen.fill(bg_color)
    font = pygame.font.Font(None, 17)
    # start main loop
    main_loop()
    # quit thread on after exiting down main loop
    rospy.signal_shutdown('Quit')
