import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Name Drawing with Turtle")
screen.bgcolor("white")

# Create and customize the turtle
pen = turtle.Turtle()
pen.speed(3)  # Set drawing speed (1-10)
pen.pensize(3)  # Set line thickness
pen.color("blue")  # Set color

# Lift the pen up - no drawing when moving
pen.penup()
# Move to starting position
pen.goto(-100, 0)
# Put the pen down to draw
pen.pendown()

# Write the name
name = "John"  # You can change this to any name
pen.write(name, font=("Arial", 36, "bold"))

# Hide the turtle cursor
pen.hideturtle()

# Alternative method to draw the name with custom style
def draw_fancy_name():
    pen.clear()  # Clear previous drawing
    pen.penup()
    pen.goto(-100, 0)
    pen.pendown()
    
    # Set style for fancy writing
    pen.color("purple")
    pen.pensize(2)
    
    # Write each letter with different colors
    colors = ["red", "blue", "green", "purple", "orange"]
    name = "Rakibulislamrefat"  # You can change this to any name
    
    x_pos = -100
    for i, letter in enumerate(name):
        pen.color(colors[i % len(colors)])
        pen.write(letter, font=("Arial", 48, "bold"))
        x_pos += 60
        pen.penup()
        pen.goto(x_pos, 0)
        pen.pendown()

# Wait for 2 seconds with the first style
time.sleep(2)

# Draw the fancy version
draw_fancy_name()

# Keep the window open
screen.mainloop() 