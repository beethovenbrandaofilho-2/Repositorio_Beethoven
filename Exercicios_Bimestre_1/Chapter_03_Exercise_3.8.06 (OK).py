
# coding: utf-8

# In[9]:


#Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

#An equilateral triangle
#A square
#A hexagon (six sides)
#An octagon (eight sides)

import turtle
wn = turtle.Screen()

# 1) An equilateral triangle
alex = turtle.Turtle()
for i in range (3):
    alex.forward(50)
    alex.left(120)

# 2) A square
beth = turtle.Turtle()
for i in range (4):
    beth.forward(60)
    beth.left(90)
    
# 3) A hexagon (six sides)
ceci = turtle.Turtle()
for i in range (6):
    ceci.forward(70)
    ceci.left(60)
    
# 4) An octagon (eight sides)
debra = turtle.Turtle()
for i in range (8):
    debra.forward(80)
    debra.left(45)
    
wn.mainloop()

#FALTA:
#COMANDO PARA "LIMPAR A TELA"

