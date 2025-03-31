# ROS

# Robot Simulation with ROS and Gazebo

## Mô tả
Robot di động 2 bánh với tay máy 2 bậc tự do chuyển đông xoay(rotation), tích hợp cảm biến Lidar,Camera và Encoder.

## Yêu cầu
- Ubuntu 20.04
- ROS Noetic
- Gazebo 11
- Các package phụ thuộc:
  - gazebo_ros_control
  - joint_state_controller
  - position_controllers
  - diff_drive_controller
  - robot_state_publisher
  - joint_state_publisher

## Cài đặt
1. Tạo workspace và clone repository:

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src

git clone https://github.com/your_username/your_repo_name.git
