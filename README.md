# Team MarvelMinds Final Project
   This is a final project for robot visualization and data processing using the Marvelminds GPS system for the Applications Programming for Engineers Course at the Univeristy of Texas at Austin in the Spring of 2019.   
   
   **Team:** Zahin Nambiar (@PhantomX-1), Will Castille (@WilliamCastille), Ashley Perez (@ashpereut)  

![Picture1](https://user-images.githubusercontent.com/47263802/57459649-3df9e380-7239-11e9-9020-c5372ddcf02a.png)

Source: https://marvelmind.com/product/starter-set-hw-v4-9-imu/

**Objective:**
Get the marvelmind beacons to communicate with the router. Use data from beacons to publish relevant data for path planning corrections through kalman filters. Even though one of the Hedgehog beacons has an IMU, the data is very noisy. Developing code to calculate pose will reduce error for state analysis.

**Packages:**  rospy, math, ros marvelmind package.

![ROS Package Visualization](https://user-images.githubusercontent.com/47263802/57459469-ed828600-7238-11e9-8958-a1e0069008f1.JPG)

**The Deliverables:** Our computer receives the location data and we can successfully calculate the pose. Pose will be published to a rostopic for another program to access. 

**Project Uniqueness:** Very little prior research on holonomic drive controls.  

![roboto](https://user-images.githubusercontent.com/47263802/57477728-ee2e1300-725e-11e9-8a22-b00d0871cc57.JPG) 

   An image of the holonomic robot that is going to be used with this program is provided. The robot is a radiation centry drone that is meant to perform perimeters around the room to check radiation levels.  

___

## Getting Started and Method

   1. Follow ROS tutorials for ROS Kinetic Kame and set-up workspace:  
   
     * Official ROS wiki: http://wiki.ros.org/ROS/Introduction  
     * ROS Tutorial: http://wiki.ros.org/ROS/Tutorials  
   
   ![ros download](https://user-images.githubusercontent.com/47263802/57472704-c1283300-7253-11e9-9e4e-132721617954.png)
   
   2. Read MarvelMind Documentation and set up Dashboard  
   
     * Package set-up: https://marvelmind.com/pics/marvelmind_ros_v2016_09_11a.pdf  
     * MarelMinds Manual: https://marvelmind.com/pics/marvelmind_navigation_system_manual.pdf  
     
  ![Capture](https://user-images.githubusercontent.com/47263802/57472770-ec128700-7253-11e9-9f5c-9e106f222c5c.JPG)
   
   3. Generate angle calculations for robot pose  
   
   ![tan](https://user-images.githubusercontent.com/47263802/57461204-35ef7300-723c-11e9-9fc0-ceda7af24178.png)
   
   Source: https://www.mathopenref.com/triggraphtan.html  
   
___
## Project Results

### Code Structure

   All the code written and contributed to for this project was written in Python. The starting files for the MarvelMind Indoor GPS System includes files in C++ but since ROS is code agnostic, our pose calculator runs with the device set-up files. Our code strucutre can be broken down into three main sections aside from the calling the packages and the main loop. The three main sections include:  
   
  * Subscribing to the hedgehog (mobile) beacons
  * Initialilzing our calculator node
  * Pose and position calculation and output  
  
   The way the code works is such that two functions were created, one for the collection of data from the beacons, called 'callback1' and another for the pose and positition calculation called 'pose'. The initialized variables are set up such that the program loops and first checks to see if the beacons are outputing data to the message file from the hedge_rcv_bin node. Then, once data indicates that the beacon is subscribing, a cycle starts in the subscribing to the hedgehog beacon section. The program uses a 'counter' variable to ensure that once one beacon's data is collected, the second beacon's data is collected after. The 'counter' is then reset to maintain this cycle. Every time a cycle is completed, the pose function is conditioned to run a position and pose calculation. The calculation is performed and outputed to two separate topics for each calcuation.

![code structure](https://user-images.githubusercontent.com/47263802/57475210-78737880-7259-11e9-998a-81954acd23d4.JPG)

   An image of the code breakdown is provided. The code cycles as described and the three main sections are highlighted in the red boxes.  
   
### Our Contribution to the World

   Overall, the project scope was to create an additional node, therefore additional functionality for the MarvelMinds Indoor GPS system and provide data that would be useful for a robotic control system.  

![calculator ros flow](https://user-images.githubusercontent.com/47263802/57477096-8cb97480-725d-11e9-9b83-191e88fe0827.JPG)

   A diagram of our project contribution to the world is provided. We met our project requirements and hope that it may be useful to other scholars studying indoor gps localization and robotic positioning.  
   
   We learned a great deal about ROS and the MarvelMind indoor navigation system!  
