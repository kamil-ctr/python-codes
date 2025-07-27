import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle for drawing
doll = turtle.Turtle()
doll.speed(3)

# Function to draw a circle
def draw_circle(t, color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color(color)
    t.circle(radius)
    t.end_fill()

# Function to draw a rectangle
def draw_rectangle(t, color, width, height, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Drawing the doll's head (circle)
draw_circle(doll, "peachpuff", 50, 0, -50)

# Drawing the doll's body (rectangle)
draw_rectangle(doll, "lightpink", 100, 150, -50, -150)

# Drawing the doll's left eye (small circle)
draw_circle(doll, "white", 10, -20, -20)

# Drawing the doll's right eye (small circle)
draw_circle(doll, "white", 10, 20, -20)

# Drawing the pupils (black circles)
draw_circle(doll, "black", 5, -20, -20)
draw_circle(doll, "black", 5, 20, -20)

# Drawing the doll's smile
doll.penup()
doll.goto(-20, -40)
doll.pendown()
doll.setheading(-60)
doll.circle(20, 120)

# Drawing the doll's arms (rectangles)
draw_rectangle(doll, "lightpink", 20, 80, -70, -140)  # Left arm
draw_rectangle(doll, "lightpink", 20, 80, 50, -140)   # Right arm

# Drawing the doll's legs (rectangles)
draw_rectangle(doll, "lightblue", 25, 80, -40, -300)  # Left leg
draw_rectangle(doll, "lightblue", 25, 80, 15, -300)   # Right leg

# Hide the turtle
doll.hideturtle()

# Keep the window open until clicked
screen.exitonclick()