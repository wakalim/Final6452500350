#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String



frame = Tk()
frame.title("Turtle_Control")
frame.geometry("200x300")

rospy.init_node("GUI_Turtle_Control")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)

    

def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	pub.botton(msg)
	
def bw():
	print("bw")
	cmd = Twist()
	cmd.linear.x = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	pub.botton(msg)

def lt():
	print("lt")
	cmd = Twist()
	cmd.linear.x = 0.0
	cmd.angular.z= 1.0
	pub.publish(cmd)
	pub.botton(msg)
	
def rt():
	print("rt")
	cmd = Twist()
	cmd.linear.x = 0
	cmd.angular.z= -1.0
	pub.publish(cmd)
	pub.botton(msg)
def on():
	print("on")
	pub.botton(msg)

def off():	
	print("off")
	pub.botton(msg)

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=120)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=230)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=180)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=180)

B5 = Button(text = "on", command=on)
B5.place(x=0, y=0)

B6 = Button(text = "off", command=off)
B6.place(x=160, y=0)

frame.mainloop()    
