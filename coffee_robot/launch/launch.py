import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Constants for paths to different files and folders
    package_name = 'coffee_robot'
    robot_name_in_model = 'coffee_robot'
    sdf_model_path = 'models/coffee_robot/robot.sdf'
    world_file_path = 'worlds/world.sdf'

    # Pose where we want to spawn the robot
    spawn_x_val = '0.0'
    spawn_y_val = '0.0'
    spawn_z_val = '0.0'
    spawn_yaw_val = '0.0'

    # Set the path to different files and folders. 
    pkg_share = FindPackageShare(package=package_name).find(package_name)
    world_path = os.path.join(pkg_share, world_file_path)
    sdf_model_path = os.path.join(pkg_share, sdf_model_path)
    os.environ["GAZEBO_MODEL_PATH"] = os.path.join(pkg_share, 'models')

    # Launch configuration variables specific to simulation
    headless = LaunchConfiguration('headless')

    return LaunchDescription([
        DeclareLaunchArgument(
            'headless',
            default_value='False',
            description='Whether to execute gzclient'),

        ExecuteProcess(
            cmd=['ign', 'gazebo', '--verbose', world_path, '-s', 'libgazebo_ros_factory.so'], output='screen'),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', robot_name_in_model, '-file', sdf_model_path, '-x', spawn_x_val, '-y', spawn_y_val, '-z', spawn_z_val, '-Y', spawn_yaw_val],
            output='screen'),
    ])
