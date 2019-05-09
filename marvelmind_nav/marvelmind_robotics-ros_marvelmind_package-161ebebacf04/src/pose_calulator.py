#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
from marvelmind_nav.msg import hedge_pos_a 
import time
import math



def callback1(data):
    global counter
    global ready
    global x1
    global x2
    global y1
    global y2
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.x_m)
    if counter == 0: #if first values not assigned:
        
        x1 = data.x_m    #Fill with appropriate data cells of node data
        y1 = data.y_m    #Fill with appropriate data cells of node data
        print(x1,y1,'1st')
        counter = counter + 1
    else:           #assign second values
        
        x2 = data.x_m    #Fill with appropriate data cells of node data
        y2 = data.y_m    #Fill with appropriate data cells of node data
        print(x2,y2,'2nd')
        counter = 0
        ready = True



def pose():
    rospy.init_node('calculator', anonymous = True)
    rospy.Subscriber("hedge_pos_a", callback = callback1, data_class = hedge_pos_a)  #Replace hedge 1 and 2 with actual ids...
    pub = rospy.Publisher("robot_pose", Float64, queue_size = 10)
    pub1 = rospy.Publisher("robot_pos", Float64MultiArray, queue_size = 10)
    global ready
    global x1
    global x2
    global y1
    global y2
    rospy.Rate(250)     #Sets rate of pose to 250 Hz faster than hedge output single message rate. only publishes when boolean is true
    
    while not rospy.is_shutdown():
        

        if counter == 0 and ready is True:
            ready = False
            pose1 = math.degrees(math.atan2((y2 - y1),(x2-x1)))
            pos1 = [((x1+x2)/2),((y1 +y2)/2)]
            array = Float64MultiArray(data = pos1)
            #if x2 >= x1 and y2 >= y1 :  #Quadrant1 output [0-90]
                #pose1 = math.degrees(math.atan( (y2 - y1)/(x2 - x1) ))
            #if x2 >= x1 and y2 < y1:  #Quadrant4 output [270,360)
                #pose1 = 360 + math.degrees(math.atan( (y2 - y1)/(x2 - x1) ))    
            #if x2 < x1 and y2 >= y1:   #Quadrant2 output (90,180]
                #pose1 = 180 + math.degrees(math.atan( (y2 - y1)/(x2 - x1) ))
            #if x2 < x1 and y2 < y1:    #Quadrant3 output (180,270)
                #pose1 = 180 + math.degrees(math.atan( (y2 - y1)/(x2 - x1) ))
            
            
            pub.publish(pose1)
            pub1.publish(array)
        
        
    rospy.spin()    #loops
if __name__ == '__main__':
   x1 = 5.0
   x2 = 7.0
   y1 = 0.0
   y2 = 0.0
   counter = 0
   pose1 = float(0.0)
   ready = False
   pose()