#!/usr/bin/env python






class Robot:

    def __init__(self):
        """"
        Set up the node here

        """

    def nav_to_pose(self, goal):
        # type: (PoseStamped) -> None
        """
        This is a callback function. It should extract data from goal, drive in a striaght line to reach the goal and
        then spin to match the goal orientation.
        :param goal: PoseStamped
        :return:
        """
        now = rospy.Time.now()
        self._odom_list.waitForTransform('base_link', 'odom', now, rospy.Duration(1))
        transGoal = self._odom_list.transformPose('base_link', goal)

        (goal_angle_roll, goal_angle_pitch, goal_angle_yaw) = tf.transformations.euler_from_quaternion(
                                                                                [transGoal.pose.orientation.x,
                                                                                 transGoal.pose.orientation.y,
                                                                                 transGoal.pose.orientation.z,
                                                                                 transGoal.pose.orientation.w])
 

    def drive_straight(self, speed, distance):
        """
        Make the turtlebot drive shraight
        :type speed: float
        :type distance: float
        :param speed: speed to drive
        :param distance: distance to drive
        :return:
        """


  

    def rotate(self, angle):
        """
        Rotate in place
        :param angle: angle to rotate
        :return:
        """



    def odom_callback(self, msg):

        """
        update the state of the robot
        :type msg: Odom
        :return:
        """
 



if __name__ == '__main__':
  pass
