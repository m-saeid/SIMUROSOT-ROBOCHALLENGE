# The_Last_of_Us 2023
Artificial intelligence and robotics competition, SIMUROSOT ROBO CHANLLENGE ,The Last of Us 2023
![image](https://github.com/m-saeid/SIMUROSOT-ROBOCHALLENGE/blob/main/The%20Last%20of%20Us.jpeg) 

# Q/A
Feel free to ask questions
   im.saeid2@gmail.com
   
  # SIMUROSOT ROBO CHANLLENGE 

--------
# Tutorials, simulator environment models and rules:
https://drive.google.com/drive/folders/15u1_yyYWXcLnS4ySjulXfdNjZMhOPSgv?usp=share_link

--------



This is the The Last of Us 2023 competition: Simurosot RoboChallenge Simulation Platform

OS: ubuntu 16.04<br>
note : It is strongly recommended not to install the OS on a(any) Virtual Machinet. Because it may cause problems.

ROS: Kinectic

--------

## 1. ROS:
You can go to:  http://wiki.ros.org/kinetic/Installation/Ubuntu
for how to download the ROS Kinetic version.<br>
Here we copy some of the proceed below:<br>

Note: This version of ROS(kinetic) ONLY supports Wily (Ubuntu 15.10), Xenial (Ubuntu 16.04) and Jessie (Debian 8) for debian packages.

1. Setup your sources.list

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
2. Setup your keys
```
sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
3. Installation
```
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
```
4. Initialize rosdep
```
sudo rosdep init
rosdep update
```
5. Environment setup
```
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## 2. Turtlebot & Gazebo Package
```
sudo apt-get install ros-kinetic-turtlebot-gazebo
```

## 3. SIMUROSOT-ROBOCHALLENGE
### 3.1 Download this project
### 3.2 Add the modles
To create access. Terminal:
```
sudo nautilus
```
go to Compuetr => /usr/share/gazebo-7/models sub-directory. Copy the all models(folders) in the models folder of this repository to this directory(/usr/share/gazebo-7/models).

### 3.3 Run the program <br>
```
python ./start.py 5 2
```

If you see the figure as follow, you are success.
![image](https://github.com/m-saeid/The_Last_of_Us/blob/main/city.png) 

## 4. File Explain 
### 4.1 The file structure 

./ros_scripts<br>
├── how_to_run.py<br>
├── robot.py<br>
├── start.py<br>
├── detect_face.py<br>
└── world.world<br>

## 4.2 detail explain for the file
#### 1. start.py
This is the start-up script. When it is running, it will start all the necessary program. After start, the Turtlebot will act according to what defined in the how_to_run.py script.
#### 2. how_to_run.py
This script define how the turtlebot act. There is only one function `Run` in this script, The function has a `robot` parameter, which is an object of class `Robot`. In this object, some act are define for manipulate the Turtlebot. The `start.py` script will be called by start-up script, and also tranfer the `robot` object.

#### 3. robot.py
The script define a `Robot` class, which wrap some basic function for the manipulation of turtlebot.

set_move_speed(met_per_sec)　: Set the speed of turtlebot，dimension is m/s.

set_turn_speed(deg_per_sec)　: Set the rotate speed of turtlebot, dimension is degree/s.

go_forward(seconds)　　　　 : Let the turtlebot move for `seconds` seconds at the given speed.

turn_around(seconds)　　　　: Let the turtlebot turn around for `seconds` seconds at the given rotate speed.

get_image()　　　　　　　　: Get the current image from camera. The image contain the RGB information as a 2D matrix.
#### 4. detect_face.py
This file is for detecting face images in the images received from the camera sensor.
#### 5. world.world
This file define the enviroment which include play field and obstacles. It will be called by "start.py" script. We have defined some more testing enviroment in the `world` sub-directory. You can use them for testing. 

## 4.3 More to do
The given demo is simple for beginners to start up. You can define more sophisticate function based on `robot.move_cmd` and `robot.turn_cmd` to set. And using `robot.cmd_vel.publish(robot.move_cmd)` to publish you manipulation. Such as simulatanious turn around and moving.
