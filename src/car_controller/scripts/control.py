#!/usr/bin/env python
import rospy
import Adafruit_PCA9685
from keyboard_controller.msg import ctrl_cmd

# set HW constants -> TODO tune max values
PWM_STEER_CH        = 0
PWM_THROT_CH        = 1
PWM_FREQ            = 100
PWM_THROT_NEUTRAL   = 600
PWM_THROT_MAX_FWD   = 700
PWM_THROT_MAX_BWD   = 530
PWM_STEER_NEUTRAL   = 650
PWM_STEER_MAX_LEFT  = 780
PWM_STEER_MAX_RIGHT = 530

def callback(data):
    # set throttle value
    range_t = int((PWM_THROT_MAX_FWD - PWM_THROT_MAX_BWD)/2)
    throttle = PWM_THROT_NEUTRAL + int(data.throttle*range_t)
    # throttle = (data.throttle * PWM_THROT_MAX_FWD if data.throttle > 0.0 else data.throttle * PWM_THROT_MAX_BWD) + PWM_THROT_NEUTRAL
    pwm.set_pwm(PWM_THROT_CH, 0, throttle)

    # set steering value
    range_s = int((PWM_STEER_MAX_LEFT - PWM_STEER_MAX_RIGHT)/2)
    steer = PWM_STEER_NEUTRAL - int(data.steer*range_s)
    # steer = (data.steer * PWM_STEER_MAX_RIGHT if data.steer > 0.0 else data.steer * PWM_STEER_MAX_LEFT) + PWM_STEER_NEUTRAL
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
