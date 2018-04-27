
# coding: utf-8

# In[12]:


# In games, we often put a rectangular “bounding box” around our sprites. 
# (A sprite is an object that can move about in the game, as we will see shortly.) 
# We can then do collision detection between, say, bombs and spaceships, by comparing whether their rectangles overlap anywhere.

# Write a function to determine whether two rectangles collide. Hint: this might be quite a tough exercise! 
# Think carefully about all the cases before you code.

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        
def collide(R1, R2):
    collision = 0
    if R2.x >= R1.x and R2.x <= R1.x + R1.width and R2.y >= R1.y and R2.y <= R1.y + R1.height:
        collision = 1
    if R2.x + R2.width >= R1.x and R2.x + R2.width <= R1.x + R1.width and R2.y >= R1.y and R2.y <= R1.y + R1.height:
        collision = 1
    if R2.x >= R1.x and R2.x <= R1.x + R1.width and R2.y + R2.height >= R1.y and R2.y + R2.height <= R1.y + R1.height:
        collision = 1
    if R2.x + R2.width >= R1.x and R2.x + R2.width <= R1.x + R1.width and R2.y + R2.height >= R1.y and R2.y + R2.height <= R1.y + R1.height:
        collision = 1
    return collision
    
R1 = Rectangle(0, 0, 20, 10)
R2 = Rectangle(0, 50, 20, 10)
collision =  collide(R1, R2)

if collision:
    print("Rectangles do collide!")
else:
    print("Rectangles don't collide!")

