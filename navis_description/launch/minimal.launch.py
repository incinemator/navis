# minimal_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                'robot_description': os.popen('xacro home/painkiller/ros2_ws/src/navis/navis_description/urdf/robots/navis.urdf.xacro').read()
            }]
        )
    ])
