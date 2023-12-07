import turtle
import random
class Polygon:
    def __init__(self,num_sides):
        self.size = random.randint(50, 150)
        self.num_side=num_sides
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.border_size = random.randint(1, 10)
    def draw_polygon(self,color):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_side):
            turtle.forward(self.size)
            turtle.left(360/self.num_side)
        turtle.penup()
    def draw_triple_polygon(self,color):
        for i in range(3):
            self.draw_polygon(color)
            self.size=self.size*0.618
            if self.num_side==3:
                self.location=[self.location[0]+10,self.location[1]+10]
            elif self.num_side==4:
                self.location=[self.location[0]+10,self.location[1]+10]
            elif self.num_side==5:
                self.location=[self.location[0]+10,self.location[1]+10]                        

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
art=int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive : "))
if art == 1:
    for i in range(30):
        num_sides = 3 # triangle
        Triangle=Polygon(num_sides)
        color=get_new_color()
        Triangle.draw_polygon(color)
elif art == 2:
    for i in range(30):
        num_sides=4
        Square=Polygon(num_sides)
        color=get_new_color()
        Square.draw_polygon(color)
elif art == 3:
    for i in range(30):
        num_sides=5
        Pentagon=Polygon(num_sides)
        color=get_new_color()
        Pentagon.draw_polygon(color)
elif art == 4:
    for i in range(30):
        num_sides=random.randint(3,5)
        Poly=Polygon(num_sides)
        color=get_new_color()
        Poly.draw_polygon(color)
elif art == 5:
    for i in range(10):
        num_sides=3
        Triangle=Polygon(num_sides)
        color=get_new_color()
        Triangle.draw_triple_polygon(color)
elif art == 6:
    for i in range(10):
        num_sides=4
        Square=Polygon(num_sides)
        color=get_new_color()
        Square.draw_triple_polygon(color)
elif art == 7:
    for i in range(10):
        num_sides=5
        Pentagon=Polygon(num_sides)
        color=get_new_color()
        Pentagon.draw_triple_polygon(color)
elif art == 8:
    for i in range(10):
        num_sides=random.randint(3,5)
        Poly=Polygon(num_sides)
        color=get_new_color()
        Poly.draw_triple_polygon(color)
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = get_new_color()
# border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.left(90)
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.right(90)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
# size *= reduction_ratio

# draw the second polygon embedded inside the original 
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()