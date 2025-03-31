#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty
import time

msg = """
==============================
 Điều khiển robot bằng phím:
------------------------------
W: Tiến
S: Lùi
A: Rẽ trái (xoay tại chỗ)
D: Rẽ phải
Q: Dừng lại
CTRL+C: Thoát
==============================
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.05)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('teleop_keyboard_fixed', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(20)

    linear_speed = 5.0
    angular_speed = 3.0
    twist = Twist()

    print(msg)

    try:
        while not rospy.is_shutdown():
            key = getKey()

            if key == 'w':
                twist.linear.x = linear_speed
                twist.angular.z = 0.0
            elif key == 's':
                twist.linear.x = -linear_speed
                twist.angular.z = 0.0
            elif key == 'a':
                twist.linear.x = 0.0
                twist.angular.z = angular_speed
            elif key == 'd':
                twist.linear.x = 0.0
                twist.angular.z = -angular_speed
            elif key == 'q':
                twist = Twist()
            else:
                twist.linear.x = 0.0
                twist.angular.z = 0.0

            pub.publish(twist)
            rate.sleep()

    except Exception as e:
        print(e)

    finally:
        pub.publish(Twist())
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)