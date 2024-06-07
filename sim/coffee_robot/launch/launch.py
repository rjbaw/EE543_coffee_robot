import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    package_share_directory = get_package_share_directory("coffee_robot")
    world_path = os.path.join(package_share_directory, "models", "world.sdf")
    robot_path = os.path.join(package_share_directory, "models", "robot.sdf")

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
                    "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock"
                    ],
                output="screen",
                ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                arguments=[
                    "/world/shapes/dynamic_pose/info@geometry_msgs/msg/PoseArray@gz.msgs.Pose_V"
                    ],
                output="screen",
            ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                arguments=[
                    "/dd1@std_msgs/msg/Float64@ignition.msgs.Double"
                    ],
                output="screen",
            ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                arguments=[
                    "/dtheta2@std_msgs/msg/Float64@ignition.msgs.Double"
                    ],
                output="screen",
            ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                arguments=[
                    "/dtheta3@std_msgs/msg/Float64@ignition.msgs.Double"
                    ],
                output="screen",
            ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                arguments=[
                    "/dtheta4@std_msgs/msg/Float64@ignition.msgs.Double"
                    ],
                output="screen",
            ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                arguments=[
                    "/dtheta5@std_msgs/msg/Float64@ignition.msgs.Double"
                    ],
                output="screen",
            ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                arguments=[
                    "/dtheta6@std_msgs/msg/Float64@ignition.msgs.Double"
                    ],
                output="screen",
            ),
        ]
    )
