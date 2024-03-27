# Voice-Controlled Autonomous Robot

This project demonstrates a Voice-Controlled Autonomous Robot capable of navigating and performing tasks based on voice commands. The robot is integrated with ROS 2 for navigation and control, and utilizes speech recognition to interpret voice commands.

## Description

The Voice-Controlled Autonomous Robot is designed to showcase the integration of voice command capabilities with autonomous navigation in robotics. Using ROS 2, the robot can navigate its environment and perform various tasks based on user voice commands. This project serves as a demonstration of the potential applications of voice-controlled robotics in various domains.

## Installation and Usage

To run the project, follow these steps:

1. Create a ROS2 workspace:
   ```bash
   mkdir vbot
   cd vbot
   mkdir src
   colcon build
   ```
1. Clone the repository into the src directory:
    ```bash
    cd src
    git clone https://github.com/irohan0/Voicebot.git
    cd ..
    colcon build
    ```
1. Build the workspace:
    ```bash
    cd ..
    colcon build
    ```
1. Source the workspace:
    ```bash
    source install/setup.bash
    ```
1. Launch the Gazebo simulation with TurtleBot3 Waffle in World 1:
    ```bash
    ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
    ```
1. Run the voice command node:
    ```bash
    ros2 run advbot voicepart
    ```
## Requirements

- ROS 2
- Gazebo
- TurtleBot3 packages
- Python 3
- speech_recognition library

## Contributors

- [Rohan Inamdar](https://github.com/irohan0)
- [Kavin Sundarr](https://github.com/KavinSundarr)
