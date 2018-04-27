
# coding: utf-8

# In[13]:


# Add a method slope_from_origin which returns the slope of the line joining the origin to the point. For example,

# >>> Point(4, 10).slope_from_origin()
# 2.5

# What cases will cause this method to fail?

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def slope_from_origin(self):
        if self.x is not 0: # problem when x = 0 (tg = infinite)
            return (self.y/self.x)

m = Point(4, 10).slope_from_origin()
print (m)

