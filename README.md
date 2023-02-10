# The_Last_of_Us
Artificial intelligence and robotics competition, SIMUROSOT ROBO CHANLLENGE ,The Last of Us 2023

# Q/A
Feel free to ask questions
   im.saeid2@gmail.com
   
  # SIMUROSOT ROBO CHANLLENGE 

--------

This is the The Last of Us 2023 competition: Simurosot RoboChallenge Simulation Platform

OS: ubuntu 16.04

ROS: Kinectic

OS:
#### : It is strongly recommended not to install the OS on a(any) Virtual Machinet. Because it may cause problems.

ROS:
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
In your home directory, Press Ctrl+H to show the hidden directory, then go to gazebo/models sub-directory. Copy the colorbox, models/newbox and models/newfield to this directory.

### 3.3 Run the program <br>
```
python ./start.py 1 1
```

If you see the figure as follow, you are success.
![image](https://github.com/zerowind168/SIMUROSOT-ROBOCHALLENGE/blob/master/roboc.png) 
