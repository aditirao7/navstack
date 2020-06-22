# Gazebo Simulation
  Gazebo simulation of a bot equipped with GPS navigation using navigation stack.
  
## How to Run
   1. Clone repo inside workspacen src.
   2. Run
      ```bash
         catkin_make
         source devel/setup.bash
      ```
   3. Run the following commands on separate terminals:
      ```bash
         roslaunch mybot_gazebo mybot_world.launch
         roslaunch mybot_navigation localization.launch
         roslaunch mybot_description mybot_rviz_amcl.launch
         rosrun mybot_navigation goal.py 49.9000357573 8.8999449505
      ```

