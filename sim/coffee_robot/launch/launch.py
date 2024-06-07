import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    package_share_directory = get_package_share_directory("coffee_robot")
    world_path = os.path.join(package_share_directory, "models", "world.sdf")
    robot_path = os.path.join(package_share_directory, "models", "robot.sdf")
    bridge_path = os.path.join(package_share_directory, "launch", "bridge.yaml")

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["ign", "gazebo", "--verbose", "-r", world_path], 
                output="screen",
            ),
            Node(
                package="ros_gz_sim",
                executable="create",
                arguments=["-name", "coffee_robot", "-file", robot_path],
                output="screen",
            ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                arguments=[
                    "--ros-args",
                    "-p",
                    "config_file:={}".format(bridge_path),
                    ],
                output="screen",
            ),
        ]
    )
