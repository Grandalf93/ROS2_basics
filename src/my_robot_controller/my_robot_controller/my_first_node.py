#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node): #The node inherits from the node class of rclpy
    
    def __init__(self):
        super().__init__("first_node")
        self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        self.get_logger().info("Hello")
        

def main(args=None):
    rclpy.init(args=args) #Initialize ROS2 communications    
    node = MyNode()
    rclpy.spin(node) #Keep the node alive, makes sure the callbacks are ued   
    rclpy.shutdown() #shutdown ROS2 communications
    

if __name__=='__main__':
    main()