#!/usr/bin/env python
import rospy 
from std_msgs.msg import String
import random
import time
import math

def talker():
    t = time.time()
    pub = rospy.Publisher('inst_pos', String, queue_size=10)
    rospy.init_node('mimic_hedgehog', anonymous=True)
    rate = rospy.Rate(10)
    x1 = 0
    y1 = 0
    z1 = 0
    p = 0 

    while not rospy.is_shutdown():
           
        x = 2*math.sin(p)   
        #x = 2*random.random()
        y = 2*math.cos(p)
        p = p+.1
        z = 6* random.random()
        t2 = time.time()
        output = '{}, {}, X={}, Y={}, Z={}'.format(str(t2),str(t2-t),str(x1),str(y1),str(z1))
        rospy.loginfo(output)
        pub.publish(output)
        x1 = x #+ x1
        y1 = y #+y1
        z1 = z1 + z 
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass