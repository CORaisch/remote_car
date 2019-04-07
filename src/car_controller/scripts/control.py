#!/usr/bin/env python
import rospy
import Adafruit_PCA9685
from keyboard_input.msg import ctrl_cmd

# set HW constants -> TODO tune max values
PWM_STEER_CH        = 0
PWM_THROT_CH        = 1
PWM_FREQ            = 100
PWM_THROT_NEUTRAL   = 600
PWM_THROT_MAX_FWD   = 650
PWM_THROT_MAX_BWD   = 550
PWM_STEER_NEUTRAL   = 650
PWM_STEER_MAX_LEFT  = 750
PWM_STEER_MAX_RIGHT = 550

def callback(data):
    # set throttle value
    range_t = int((PWM_THROT_MAX_FWD - PWM_THROT_MAX_BWD)/2)
    throttle = PWM_THROT_NEUTRAL + int(data.throttle)*range_t
    pwm.set_pwm(PWM_THROT_CH, 0, throttle)

    # set steering value
    range_s = int((PWM_STEER_MAX_LEFT - PWM_STEER_MAX_RIGHT)/2)
    steer = PWM_STEER_NEUTRAL - int(data.steer)*range_s
    pwm.set_pwm(PWM_STEER_CH, 0, steer)

    # debug
    print('throttle: {0}, steer: {1}'.format(throttle, steer))

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("ctrl_cmd", ctrl_cmd, callback)
    rospy.spin()

if __name__ == '__main__':
    # init PWM signals
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(PWM_FREQ)

    # run control loop
    listener()
