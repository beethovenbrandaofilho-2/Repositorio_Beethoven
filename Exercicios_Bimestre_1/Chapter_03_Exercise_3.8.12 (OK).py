
# coding: utf-8

# In[1]:


#Write a program to draw a face of a clock that looks something like this:
#...

import turtle
wn = turtle.Screen()

alex = turtle.Turtle()
alex.forward(50)
alex.forward(-50)
for i in range (11):
    alex.left(30)
    alex.forward(50)
    alex.forward(-50)
    
wn.mainloop()

