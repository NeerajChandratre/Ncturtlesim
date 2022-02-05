#!/usr/bin/env python
#!/usr/bin/env python
from __future__ import print_function
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
from turtlesim.srv import Spawn,Kill
class TurtleBot:

    def service_kill(self):
            killing_the_turtle = rospy.ServiceProxy('/kill',Kill)
            rospy.wait_for_service('/kill')
            self.tname = "turtle1"
            killing_the_turtle(self.tname)

    def start(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/Neeraj/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/Neeraj/cmd_vel',Twist, queue_size=10)

        # A subscriber to the topic '/Neeraj/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/Neeraj/pose',Pose, self.update_pose)
        self.rate = rospy.Rate(10)

    def robot_spawning(self):
        print("Enter 0 for spawning a robot at a predetermined location.")
        print("Enter 1 for spawning a robot at your given location.")
        wish = int(input("Enter 0 or 1?:- "))
        if wish == 1:
            for s in range (1):
                print("Enter the spawn co-ordinates")
                self.f1 = float(input("Enter x co-ordinate:- "))
                self.f2 = float(input("Enter y co-ordinate:- "))
                self.f3 = float(input("Enter angle "))
                if self.f1 > 10.5 or self.f2 > 9 or self.f1 <= 0.7 or self.f2 <= 0.7:
                    print("Out of bounds! Setting the robot at our predetermined location")
                    wish = 0
                self.f4 = "Neeraj"
        if wish == 0:
            self.f1 = 2.54
            self.f2 = 0.54
            self.f3 = 0
            self.f4 = "Neeraj"

        new_robot = rospy.ServiceProxy('/spawn',Spawn)
        rospy.wait_for_service('/spawn')
        new_robot(self.f1,self.f2,self.f3,self.f4)
        self.pose = Pose()
        self.pose.x = self.f1
        self.pose.y = self.f2

    def update_pose(self, data): #"data" is declared here
        """Callback function which is called when a new message of type Pose is received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4) # rounding off
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return 1
    def steering_angle(self, goal_pose):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self, x , y , the_distance_tolerance):
        """Moves the turtle to the goal."""
        goal_pose = Pose()
        goal_pose.x = x
        goal_pose.y = y
        distance_tolerance = the_distance_tolerance

        vel_msg = Twist()

        while self.euclidean_distance(goal_pose) >= distance_tolerance:
            # Porportional controller.
            # https://en.wikipedia.org/wiki/Proportional_control

            # Linear velocity in the x-axis.
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.service_kill()
        x.robot_spawning()
        x.start()
        print("Enter 0 for traversing a zig-zag path or enter 1 for traversing as per your desired locations")
        selectchoice = int(input("0 or 1?:- "))
        if selectchoice == 0:
                hx = abs(float(input("Enter the horizontal distance:- ")))
                hy = abs(float(input("Enter the vertical distance:- ")))
                fx = hx + 2.54
                fy = hy + 0.54
                fhy = hy*0.5

                if fx > 13 or fy > 11.04 or fx <= 0 or fy <= 0:
                    print("Distances exceed the limits! We will take a safe traverse to avoid collision")
                    x.move2goal(10.46,10.5,0.32)
                    x.move2goal(2.54,10.5,0.32)
                    x.move2goal(2.54,5.25,0.32)
                    x.move2goal(10.46,5.25,0.32)
                    x.move2goal(10.46,0.54,0.32)
                    x.move2goal(2.54,0.54,0.32)

                if fx <= 13 and fy <= 11.04 and fx > 0 and fy > 0:
                    print("Traversing the robot ")
                    x.move2goal(hx,hy,0.49)
                    x.move2goal(2.54,hy,0.32)
                    x.move2goal(2.54,fhy,0.32)
                    x.move2goal(hx,fhy,0.32)
                    x.move2goal(hx,0.54,0.32)
                    x.move2goal(2.54,0.54,0.32)
        if selectchoice ==1:

            print("Enter the number of locations for traversing the robot")
            loc = int(input("Enter the number of locations:- "))
            for v in range (loc):
                print("Enter the x and y co-ordinates.")
                xr = float(input("Enter the x co-ordinate:- "))
                yr = float(input("Enter the y co-ordinate:- "))
                if xr > 10.5 or yr > 9 or xr <= 0.7 or yr <= 0.7:
                    print("Out of bounds! Program will stop")
                    break
                else:
                    x.move2goal(xr,yr,1)

    except rospy.ROSInterruptException:
        pass
