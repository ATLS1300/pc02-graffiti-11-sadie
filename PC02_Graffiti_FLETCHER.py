#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
home() #turtle starts in middle of screen

# left eye (his right)
up()
goto(-15,110)
down()
color('red')
dot(10)

# right eye (his left)
up()
left(13)
forward(60)
dot(10)

# blockhead
up()
right(13)
forward(20)
down()
pensize(10)
color('blue')
right(90)
forward(120)
right(90)
forward(140)
right(90)
forward(160)
right(90)
forward(140)
right(90)
forward(40)

#yellow line
up()
right(50)
forward(250)
down()
color('yellow')
left(180)
pensize(20)
forward(300)
up()








up() #picks turtle up before returning home





