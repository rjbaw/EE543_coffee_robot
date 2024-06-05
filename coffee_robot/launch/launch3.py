from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_share_directory = get_package_share_directory('coffee_robot')
    world_path = os.path.join(package_share_directory, 'models', 'world.sdf')
    robot_path = os.path.join(package_share_directory, 'models', 'robot.sdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['ign', 'gazebo', '--verbose', '-r', world_path],
            output='screen'
        ),
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-name', 'my_robot', '-file', robot_path],
            output='screen'
        ),
    ])

