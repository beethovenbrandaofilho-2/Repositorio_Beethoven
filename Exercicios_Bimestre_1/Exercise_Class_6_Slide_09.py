
# coding: utf-8

# In[13]:


# Crie extensoes no exemplo de classes de poligonos regulares de modo a avaliar os diferentes MROs possiveis
#MRO (Method Resolution Order)

class Shape:
    geometric_type = 'Generic Shape'
    
    def get_geometric_type(self):
        return self.geometric_type
    
class Circle(Shape):
    geometric_type = 'Circle'
            
class Polygon(Shape):
    geometric_type = 'Polygon'
    
class Triangle(Polygon):
    geometric_type = 'Triangle'
    
class Rectangle(Polygon):
    geometric_type = 'Rectangle'
    
class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'
        
class RegularHexagon(RegularPolygon):
    geometric_type = 'RegularHexagon'
    
class Square(Rectangle, RegularPolygon):
    geometric_type = 'Square'
    
class EquiTriangle(Triangle, RegularPolygon):
    geometric_type = 'EquiTriangle'
    
class ChessTable(Square):
    geometric_type = 'ChessTable'

circle = Circle()
polygon = Polygon()
triangle = Triangle()
rectangle = Rectangle()
regularpolygon =  RegularPolygon()
regularhexagon = RegularHexagon()
square = Square()
equitriangle = EquiTriangle()
chesstable = ChessTable()

print(circle.geometric_type)
print(polygon.geometric_type)
print(triangle.geometric_type)
print(rectangle.geometric_type)
print(regularpolygon.geometric_type)
print(regularhexagon.geometric_type)
print(square.geometric_type)
print(equitriangle.geometric_type)
print(chesstable.geometric_type)

print("Circle: ", circle.__class__.__mro__)
print("Polygon: ", polygon.__class__.__mro__)
print("Triangle: ", triangle.__class__.__mro__)
print("Rectangle: ", rectangle.__class__.__mro__)
print("RegularPolygon: ", regularpolygon.__class__.__mro__)
print("RegularHexagon: ", regularhexagon.__class__.__mro__)
print("Square: ", square.__class__.__mro__)
print("EquiTriangle: ", equitriangle.__class__.__mro__)
print("Chess Table: ", chesstable.__class__.__mro__)

