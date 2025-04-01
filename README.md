
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
```

### 📥 Bước 2: Clone Repository

```bash
git clone https://github.com/thaithinhhl/ROS.git
cd ~/catkin_ws
mv ROS Assem2
catkin_make
```

### 🧠 Bước 3: Source workspace

```bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
## 🛰️ Mô phỏng

### 🎯 Bước 4: Khởi chạy mô phỏng trong Gazebo 

``` bash
roslaunch Assem2 gazebo.launch
```

### ⚙️ Bước 5: Load các controller cho robot 
``` bash
roslaunch Assem2 start_controllers.launch
```

### 🌐 Bước 6: Mở RViz để quan sát robot
```
roslaunch Assem2 display.launch
```

### 🦾 Bước 7: Điều khiển tay máy (Arm Controller)
Điều khiển bẳng 4 phím mũi tên trên bàn phím
```bash
rosrun Assem2 arm_teleop_keyboard
```

### 🎮 Bước 8: Điều khiển robot di chuyển

2 cách để điều khiển robot di chuyển:

---

#### 🧭 Cách 1: Gửi lệnh trực tiếp qua topic `/cmd_vel`

```bash
rostopic pub /cmd_vel geometry_msgs/Twist "linear:
  x: 3.5
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 1.5" -r 10
```
#### 🕹️ Cách 2: Chạy script điều khiển bằng bàn phím

```bash
rosrun Assem2 teleop_keyboard.py
```

### 🧾 Bước 9: Đọc giá trị encoder từ bánh xe

Có thể kiểm tra vị trí và vận tốc của các joint (bánh xe & tay máy) bằng cách đọc topic:

```bash
rostopic echo /joint_states
```
📌 Topic này cung cấp thông tin về:

  - name: tên các joint (VD: joint_L, joint_R)

  - position: vị trí hiện tại của joint (theo radian)

  - velocity: tốc độ góc hiện tại của joint (rad/s)

