# Marvel_Minds_G12
This is a final project for robot visualization and data processing using the Marvelminds GPS system for the Applications Programming for Engineers Course at the Univeristy of Texas at Austin in the Spring of 2019.

Objective: 
Get the marvelmind beacons to communicate with the router. Use data from beacons to publish relevant data for path planning corrections through kalman filters. Even though one of the Hedgehog beacons has an IMU, the data is very noisy. Developing code to calculate pose will reduce error for state analysis.

Packages:  rospy, math, time, ros marvelmind package.

The Deliverables: Our computer receives the location data and we can successfully calculate the pose. Pose will be published to a rostopic for another program to access. 

Project Uniqueness: Very little prior research on holonomic drive controls. 

