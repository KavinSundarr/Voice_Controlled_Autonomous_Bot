#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
import math

class VoiceBot(Node):
    def __init__(self):
        super().__init__('voice_bot')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.current_position = Point()
        self.initial_position = Point()
        self.initial_position_set = False

        # Vocabulary for voice commands
        # Vocabulary for voice commands
        self.command_vocabulary = {
        "forward": ["forward", "go forward", "move forward", "straight", "front", "ahead", "advance", "proceed", "onward", "forwards"],
        "backward": ["backward", "go backward", "move backward", "back", "reverse", "retreat", "behind", "rearward", "backwards", "reverse"],
        "left": ["left", "turn left", "port", "leftward", "to the left", "anticlockwise", "turn anti-clockwise", "turning left", "leftwards", "on the left"],
        "right": ["right", "turn right", "starboard", "rightward", "to the right", "clockwise", "turn clockwise", "turning right", "rightwards", "on the right"],
        "return": ["return", "go back", "come back", "retreat", "reverse", "back", "go home", "backtrack", "turn around", "revert"],
        "stop": ["stop", "halt", "cease movement", "end", "pause", "stand still", "halt movement", "freeze", "stay", "brake"]
}


        # Subscribe to the odometry topic to track the robot's position
        self.create_subscription(Point, '/odometry', self.odometry_callback, 10)

    def odometry_callback(self, msg):
        self.current_position = msg
        if not self.initial_position_set:
            self.initial_position = msg
            self.initial_position_set = True

    def execute_command(self, command):
        twist = Twist()
        for key, synonyms in self.command_vocabulary.items():
            if any(synonym in command for synonym in synonyms):
                if key == "forward":
                    twist.linear.x = 1.0
                elif key == "backward":
                    twist.linear.x = -1.0
                elif key == "left":
                    twist.angular.z = 1.0
                elif key == "right":
                    twist.angular.z = -1.0
                elif key == "return":
                    twist.linear.x = -1.0  # Move backward
                    twist.angular.z = self.calculate_angle_to_initial_position()
                elif key == "stop":
                    twist = Twist()  # Stop all motion
                break  # Exit loop once command is found
        self.publisher.publish(twist)

    def calculate_angle_to_initial_position(self):
        angle = math.atan2(self.initial_position.y - self.current_position.y,
                           self.initial_position.x - self.current_position.x)
        return angle

def main(args=None):
    rclpy.init(args=args)
    voice_bot = VoiceBot()
    rclpy.spin(voice_bot)
    voice_bot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
