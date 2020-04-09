# wir_tutorial README

-copy the entire folder into the ~/catkin_ws/src file of a computer that is set up for ROS.

	$source /opt/ros/melodic/setup.bash 
	(if not already set up as part of your bashrc)

-run catkin_make and source the build
-run the following line of code

	$ roslaunch wir_tutorial turtlebot3_autorace.launch

-Gazebo should launch and open up a robot on a track
(If it doesnt launch or you get error messages you may still have a previous rosmaster or gazebo server running, try killall rosmaster or killall gzserver)

-Open a new terminal and run

	*To run tele operated robot
	$ rosrun wir_tutorial teleop_robot.py

	
	*To run simple robot that drives in circles
	$ rosrun wir_tutorial circle.py 
 

