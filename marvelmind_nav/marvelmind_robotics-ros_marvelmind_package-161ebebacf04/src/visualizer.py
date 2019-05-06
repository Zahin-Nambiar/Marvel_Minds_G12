#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time
from mpl_toolkits import mplot3d
import matplotlib.ticker as ticker


def callback(data):
    a = data.data.split(',')
    x = float(a[2][3:])
    y = float(a[3][3:])
    z = float(a[4][3:])
    
    x1.append(x)
    y1.append(y)
    z1.append(z)
    
    rospy.loginfo(rospy.get_caller_id() + "I heard x is testing %s", a[2][3:])

def animate(i):
    ax.clear()
    ax.plot3D(x1,y1,z1)
    
    

def listener():


    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("inst_pos", String, callback)


    ani = animation.FuncAnimation(fig, animate, interval = 10)
    plt.show()


    rospy.spin()

if __name__ == '__main__':
    x1 = []
    y1 = []
    z1 = []
    
    
    fig = plt.figure()
    ax = plt.axes(projection='3d', autoscale_on = False)
    
    listener()
    