# Ncturtlesim
It is a basic project of operating a turtle robot in turtlesim.

## Overview
In this project, I spawned a turtle robot and later I gave the robot locations at which the robot should go. The robot goes at a constant velocity of 1 m/s. I have given flexibility 
to the user who will run this code. The flexibility includes spawning at a predetermined location or a location assigned by user. Later, the user can give the robot random locations for 
moving or the user should give the horizontal and vertical distance of traversing the zig zag path.

## Steps to run this project
- Clone the repository
- Open terminal and go to the top of the directory where the "src" folder exists, then run catkin make
- You will see "devel" and "setup" folders in the directory
- Run roscore by typing "roscore" on any terminal
- Open turtlesim using a new terminal. Type this for opening it: rosrun turtlesim turtlesim_node
- Finally, run the turtlesim python code on a new terminal. Source the .bash file when you are in the top of directory (where src folder exists) by typing source devel/setup.bash
 in the terminal. Type this command after that for running the python code: rosrun main_nchw goalpoints.py

Note:- In the last two steps, please keep this order for running the project properly. The turtlesim should start first and then the goalpoints.py python code
should run.

## Working of this project
1. The main python code consists of velocity publisher which publishes the velocity commands. There is a subscriber who sees 
the message of Pose. Later, I have used two service calls. The first call kills the turtle robot which is spawned as soon as
the turtlesim starts. The second service call is used for spawning a new turtle robot which has new x and y co-ordinates and angle theta of rotation.

2. The main code has boundary conditions for the provided value of co-ordinates and distances so that the turtle robot shouldn't collide or land up
at the walls. The while loop which is used for the robot to reach its goal positions has "tolerance" as a parameter. Also, the angular velocity calculation 
includes "constant" as a parameter. These parameters should be tuned as per the requirements of robot traverse. The tolerance parameter should not be very low
as very less tolerance values can cause the robot to be super precise which it won't handle as this python code and the simulator isn't suitable for handling 
very precise robot movements.

## Project highlights

### Robot traverse at extreme values
![Robot traverse](/output_images/1.png "Robot traverse at extreme values provided by user")

Robot traverse at extreme values values provided by user

![Robot traverse](/output_images/1_ip.png "Input of robot traverse at extreme values provided by user")

Input of robot traverse at extreme values provided by user

### Robot traverse at normal values 
![Robot traverse](/output_images/2.png "Robot traverse at normal values provided by user")

Robot traverse at normal values provided by user

![Robot traverse](/output_images/2_ip.png "Input of robot traverse at normal values provided by user")

Input of robot traverse at normal values provided by user

### Robot spawn at a point and giving it a location
![Robot traverse](/output_images/3.png "Spawning of robot at any point and giving the robot a location")

Spawning of robot at any point and giving the robot a location

![RObot traverse](/output_images/3_ip.png "Input of spawning of robot at any point and giving the robot a location")

Input of spawning of robot at any point and giving the robot a location

Note:- The zig zag patterns do not carry out a proper straight line traversal or proper angular rotations as this totally depends on the two parameters which are "tolerance" 
and "constant" which I discussed earlier.  
