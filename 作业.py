from turtle import *

def draw_star():
    speed(5)  # Set drawing speed
    bgcolor("black")  # Set background color
    pensize(2)  # Set the pen size
    pencolor("yellow")  # Set the pen color

    # Move to starting position
    penup()
    goto(-50, 0)
    pendown()

    # Begin drawing the star
    begin_fill()  # Start filling the shape
    fillcolor("yellow")  # Fill color for the star
    for _ in range(5):
        forward(100)  # Draw side of the star
        right(144)  # Angle to form a five-pointed star
    end_fill()  # End filling the shape

    # Finish drawing
    hideturtle()  # Hide the turtle cursor
    done()  # Finish the drawing and display the window

# Call the function to draw the star
draw_star()
