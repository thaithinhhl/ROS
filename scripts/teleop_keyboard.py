#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
==============================
 Điều khiển robot bằng phím:
------------------------------
W: Tiến
S: Lùi
A: Rẽ trái (xoay tại chỗ)
D: Rẽ phải
SPACE: Dừng lại
Q: Nhập số mét để di chuyển
ESC: Thoát
==============================
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.01)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def get_distance():
    print("Nhập khoảng cách (mét): ")
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    distance = input()
    try:
        return float(distance)
    except:
        print("Giá trị không hợp lệ, sử dụng giá trị mặc định 1m")
        return 1.0

if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('teleop_keyboard', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    # Khởi tạo message Twist
    twist = Twist()
    
    # Tốc độ cố định
    linear_speed = 10.0    # Tốc độ tuyến tính
    angular_speed = 20.0   # Tốc độ góc
    
    print(msg)
    
    try:
        while not rospy.is_shutdown():
            key = getKey()
            
            # Reset tốc độ về 0
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            
            if key == 'w':
                twist.linear.x = linear_speed
            elif key == 's':
                twist.linear.x = -linear_speed
            elif key == 'a':
                twist.angular.z = angular_speed
            elif key == 'd':    
                twist.angular.z = -angular_speed
            elif key == ' ':
                twist.linear.x = 0.0
                twist.angular.z = 0.0
            elif key == 'q':
                distance = get_distance()
                time_to_move = distance / linear_speed
                print(f"Di chuyển {distance}m trong {time_to_move:.2f} giây")
                twist.linear.x = linear_speed
                pub.publish(twist)
                rospy.sleep(time_to_move)
                twist.linear.x = 0.0
            elif key == '\x1b':  # Phím ESC
                break
                
            pub.publish(twist)
            rospy.sleep(0.01)
            
    except Exception as e:
        print(e)
        
    finally:
        # Dừng robot trước khi thoát
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)