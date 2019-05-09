# Team MarvelMinds Final Project
This is a final project for robot visualization and data processing using the Marvelminds GPS system for the Applications Programming for Engineers Course at the Univeristy of Texas at Austin in the Spring of 2019.

![Picture1](https://user-images.githubusercontent.com/47263802/57459649-3df9e380-7239-11e9-9020-c5372ddcf02a.png)

Objective: 
Get the marvelmind beacons to communicate with the router. Use data from beacons to publish relevant data for path planning corrections through kalman filters. Even though one of the Hedgehog beacons has an IMU, the data is very noisy. Developing code to calculate pose will reduce error for state analysis.

Packages:  rospy, math, time, ros marvelmind package.

![ROS Package Visualization](https://user-images.githubusercontent.com/47263802/57459469-ed828600-7238-11e9-8958-a1e0069008f1.JPG)

The Deliverables: Our computer receives the location data and we can successfully calculate the pose. Pose will be published to a rostopic for another program to access. 

Project Uniqueness: Very little prior research on holonomic drive controls. 


![roboto](https://user-images.githubusercontent.com/47263802/57458995-f58df600-7237-11e9-9c7c-b2e9efba145b.JPG)

___

# Getting Started and Method

   1. Follow ROS tutorials for ROS Kinetic Kame and set-up workspace:  
   
   Official ROS wiki: http://wiki.ros.org/ROS/Introduction  
   ROS Tutorial: http://wiki.ros.org/ROS/Tutorials  
   
   2. Read MarvelMind Documentation and set up Dashboard  
   
   Package set-up: https://marvelmind.com/pics/marvelmind_ros_v2016_09_11a.pdf  
   MarelMinds Manual: https://marvelmind.com/pics/marvelmind_navigation_system_manual.pdf  
   
   3. Generate angle calculations for robot pose
   
___
# Project Results

