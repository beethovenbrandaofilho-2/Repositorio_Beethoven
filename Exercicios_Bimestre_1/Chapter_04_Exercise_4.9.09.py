
# coding: utf-8

# In[17]:


#Write a void function to draw a star, where the length of each side is 100 units. 
#(Hint: You should turn the turtle by 144 degrees at each point.)

import turtle
def draw_star(t,sz):
    #t.left(36)
    #t.forward(sz)
    for i in range (5):
        t.right(144)
        t.forward(sz)

wn = turtle.Screen ()
alex = turtle.Turtle()
draw_star(alex,100)

wn.mainloop()

