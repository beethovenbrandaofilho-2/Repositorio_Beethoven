
# coding: utf-8

# In[13]:


# Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above,
# where the first item of the pair is the angle to turn, and the second item is the distance to move forward.
# Set up a list of pairs so that the turtle draws a house with a cross through the centre, as show here. 
# This should be done without going over any of the lines / edges more than once, and without lifting your pen.

import turtle
import math
wn = turtle.Screen()
alex = turtle.Turtle()

walking_data = [(180, 40), (225, math.sqrt(3200)), (75, 40), (120, 40), (75, math.sqrt(3200)), (135, 40), (90, 40), (90, 40)]

for (angle,distance) in walking_data:
    alex.left(angle)
    alex.forward(distance)
    
wn.mainloop()

