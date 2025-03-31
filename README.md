
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

## 🚀 Cài đặt

### 🔧 Bước 1: Tạo ROS Workspace

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace   
---

📥 Bước 2: Clone Repository
git clone https://github.com/thaithinhhl/ROS.git
cd ~/catkin_ws
catkin_make

🧠 Bước 3: Source workspace
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
