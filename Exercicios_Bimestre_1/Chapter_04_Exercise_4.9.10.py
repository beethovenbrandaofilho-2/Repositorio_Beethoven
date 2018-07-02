
# coding: utf-8

# In[9]:


# Extend your program above.
# Draw five stars, but between each, pick up the pen, move forward by 350 units, 
# turn right by 144, put the pen down, and draw the next star. You’ll get something like this:
#...

import turtle

def draw_star(t,sz):
    for i in range (5):
        t.forward(sz)
        t.right(144)

def change_star(tt,d):
    tt.penup()
    tt.forward(d)
    tt.right(144)
    tt.pendown()
    
wn = turtle.Screen ()
wn.bgcolor("lightgreen") 
alex = turtle.Turtle()

for i in range (5):
    draw_star(alex,100)
    change_star(alex,350)

wn.mainloop()

