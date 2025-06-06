from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get package share directory
    pkg_share = get_package_share_directory('navis_description')
    
    # URDF file path
    urdf_file = os.path.join(pkg_share, 'urdf', 'navis.urdf.xacro')
    
    return LaunchDescription([
        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            arguments=[urdf_file],
            parameters=[{'use_sim_time': False}]
        ),
        
        # RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(pkg_share, 'rviz', 'navis_display.rviz')]
        ),
        
        # Joint State Publisher GUI (for manual joint control)
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        )
    ])