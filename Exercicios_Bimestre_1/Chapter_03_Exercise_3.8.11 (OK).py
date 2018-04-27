
# coding: utf-8

# In[1]:


#Write a program to draw a shape like this:
#STAR

import turtle
wn = turtle.Screen()

alex = turtle.Turtle()
alex.left(36)
alex.forward(50)

for i in range (4):
    alex.left(144)
    alex.forward(50)

wn.mainloop()

