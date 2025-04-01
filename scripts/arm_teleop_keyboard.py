#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import sys, select, termios, tty

msg = """
==============================
 Điều khiển tay máy bằng phím:
------------------------------
Mũi tên LÊN: Tay 1 lên
Mũi tên XUỐNG: Tay 1 xuống
Mũi tên PHẢI: Tay 2 lên
Mũi tên TRÁI: Tay 2 xuống
Q: Thoát

Giới hạn góc:
Tay 1: -10.0 đến 10.0 rad
Tay 2: -10.0 đến 10.0 rad
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

def constrain(val, min_val, max_val):
    return max(min(val, max_val), min_val)

if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('arm_teleop_keyboard', anonymous=True)
    
    # Publishers cho hai tay máy
    pub_arm1 = rospy.Publisher('/arm_1_joint_controller/command', Float64, queue_size=10)
    pub_arm2 = rospy.Publisher('/arm_2_joint_controller/command', Float64, queue_size=10)
    
    # Vị trí hiện tại của các khớp
    arm1_pos = 0.0
    arm2_pos = 0.0
    
    # Giới hạn góc (radian)
    ARM1_MIN = -10.0
    ARM1_MAX = 10.0
    ARM2_MIN = -10.0
    ARM2_MAX = 10.0
    
    # Bước di chuyển mỗi lần nhấn phím (radian)
    step = 0.2
    
    print(msg)
    
    try:
        while not rospy.is_shutdown():
            key = getKey()
            if key == '\x1b':
                key = getKey()
                if key == '[':
                    key = getKey()
                    if key == 'A':  # Mũi tên lên
                        arm1_pos = constrain(arm1_pos + step, ARM1_MIN, ARM1_MAX)
                        pub_arm1.publish(Float64(arm1_pos))
                        print(f"Tay 1: {arm1_pos:.2f} rad [{ARM1_MIN} đến {ARM1_MAX}]")
                    elif key == 'B':  # Mũi tên xuống
                        arm1_pos = constrain(arm1_pos - step, ARM1_MIN, ARM1_MAX)
                        pub_arm1.publish(Float64(arm1_pos))
                        print(f"Tay 1: {arm1_pos:.2f} rad [{ARM1_MIN} đến {ARM1_MAX}]")
                    elif key == 'C':  # Mũi tên phải
                        arm2_pos = constrain(arm2_pos + step, ARM2_MIN, ARM2_MAX)
                        pub_arm2.publish(Float64(arm2_pos))
                        print(f"Tay 2: {arm2_pos:.2f} rad [{ARM2_MIN} đến {ARM2_MAX}]")
                    elif key == 'D':  # Mũi tên trái
                        arm2_pos = constrain(arm2_pos - step, ARM2_MIN, ARM2_MAX)
                        pub_arm2.publish(Float64(arm2_pos))
                        print(f"Tay 2: {arm2_pos:.2f} rad [{ARM2_MIN} đến {ARM2_MAX}]")
            elif key == 'q' or key == 'Q':
                break
            
            rospy.sleep(0.1)

    except Exception as e:
        print(e)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)