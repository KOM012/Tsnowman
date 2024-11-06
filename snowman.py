import turtle
import math

def draw_circle(t, x, y, radius):
    """Draw a circle at (x,y) with given radius"""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

def draw_rectangle(t, x, y, width, height, color="black"):
    """Draw a filled rectangle at (x,y) with given width and height"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_hand(t, x, y, direction, scale):
    """Draw a hand with three fingers"""
    t.penup()
    t.goto(x, y)
    t.setheading(direction)
    finger_length = 10 * scale
    
    # Draw palm
    t.pendown()
    t.dot(0.5 * scale)
    
    # Draw three fingers
    original_heading = t.heading()
    for angle in [-20, 0, 20]:
        t.penup()
        t.goto(x, y)
        t.setheading(original_heading + angle)
        t.pendown()
        t.forward(finger_length)

def draw_speech_bubble(t, x, y, text, scale):
    """Draw a rounded speech bubble with triangular tail pointing to origin"""
    bubble_width = 100 * scale
    bubble_height = 40 * scale
    radius = 15 * scale  # radius for rounded corners
    
    # Draw main bubble with rounded corners
    t.penup()
    t.goto(x + radius, y)  # Start at first curve position
    t.color("black")
    t.fillcolor("white")
    t.begin_fill()
    
    # Bottom side
    t.setheading(0)
    t.pendown()
    t.forward(bubble_width - 2 * radius)
    
    # Right bottom curve
    for _ in range(90):
        t.forward((2 * math.pi * radius) / 360)
        t.left(1)
    
    # Right side
    t.forward(bubble_height - 2 * radius)
    
    # Right top curve
    for _ in range(90):
        t.forward((2 * math.pi * radius) / 360)
        t.left(1)
    
    # Top side
    t.forward(bubble_width - 2 * radius)
    
    # Left top curve
    for _ in range(90):
        t.forward((2 * math.pi * radius) / 360)
        t.left(1)
    
    # Left side
    t.forward(bubble_height - 2 * radius)
    
    # Left bottom curve
    for _ in range(90):
        t.forward((2 * math.pi * radius) / 360)
        t.left(1)
    
    # Draw triangular tail
    # Calculate angle to point towards 0,0
    tail_start_x = x + bubble_width/3
    tail_start_y = y
    angle_to_origin = math.degrees(math.atan2(-tail_start_y, -tail_start_x))
    
    t.penup()
    t.goto(tail_start_x + 20 * scale, y)  # Start point of triangle
    t.setheading(angle_to_origin)
    t.pendown()
    
    # Draw triangle tail
    triangle_base = 40 * scale
    triangle_height = 20 * scale
    
    # First point is where we are
    point1 = t.position()
    # Second point is triangle_base to the right
    t.penup()
    t.goto(tail_start_x - 1 * scale, y)
    point2 = t.position()
    # Third point is towards the origin
    point3 = (tail_start_x, y - triangle_height)
    
    # Draw the triangle
    t.penup()
    t.goto(point1)
    t.pendown()
    t.goto(point3)
    t.goto(point2)
    t.goto(point1)
    
    t.end_fill()
    
    # Add text
    t.penup()
    t.goto(x + bubble_width/2, y + bubble_height/2)
    t.color("black")
    t.write("Merry Christmas!", align="center", font=("Arial", int(8 * scale), "bold"))

def draw_snowman(scale=1, speed=0):
    """Draw a snowman with customizable scale and centered features"""
    # Initialize turtle
    t = turtle.Turtle()
    t.speed(speed)
    t.color("blue")
    
    # Define proportions
    bottom_radius = 50 * scale
    middle_radius = 30 * scale
    head_radius = 20 * scale
    
    # Calculate centers of each circle
    bottom_center_y = -50 * scale
    middle_center_y = bottom_center_y + bottom_radius + middle_radius
    head_center_y = middle_center_y + middle_radius + head_radius
    
    # Draw bottom circle
    draw_circle(t, 0, bottom_center_y, bottom_radius)
    
    # Draw middle circle
    draw_circle(t, 0, middle_center_y, middle_radius)
    
    # Draw head circle
    draw_circle(t, 0, head_center_y, head_radius)
    
    # Draw enhanced hat
    hat_base_width = 40 * scale
    hat_base_height = 15 * scale
    hat_top_width = 30 * scale
    hat_top_height = 25 * scale
    hat_y = head_center_y + head_radius - (hat_base_height * 0.1)
    
    # Draw hat base (wider rectangle)
    draw_rectangle(t, -hat_base_width/2, hat_y, hat_base_width, hat_base_height)
    
    # Draw red stripe on hat base
    stripe_height = hat_base_height * 0.4
    stripe_y = hat_y + (hat_base_height - stripe_height)/2
    draw_rectangle(t, -hat_base_width/2, stripe_y, hat_base_width, stripe_height, "red")
    
    # Draw hat top (taller, thinner rectangle)
    draw_rectangle(t, -hat_top_width/2, hat_y + hat_base_height, hat_top_width, hat_top_height)
    
    # Draw eyes
    t.color("black")
    eye_y = head_center_y + (head_radius * 0.2)
    for x in [-7 * scale, 7 * scale]:
        t.penup()
        t.goto(x, eye_y)
        t.pendown()
        t.dot(5 * scale)
    
    # Draw carrot nose
    t.penup()
    t.goto(0, head_center_y)
    t.color("orange")
    t.pendown()
    t.setheading(-90)
    t.fillcolor("orange")
    t.begin_fill()
    for _ in range(3):
        t.forward(8 * scale)
        t.left(120)
    t.end_fill()
    
    # Draw buttons
    t.color("black")
    button_spacing = middle_radius * 0.6
    num_buttons = 3
    button_size = 6 * scale
    
    for i in range(num_buttons):
        button_y = middle_center_y + middle_radius - (button_spacing * (i + 0.5))
        t.penup()
        t.goto(0, button_y)
        t.pendown()
        t.dot(button_size)
    
    # Draw arms with hands
    t.color("brown")
    t.pensize(3 * scale)
    arm_length = 40 * scale
    
    # Left arm and hand
    t.penup()
    t.goto(-middle_radius, middle_center_y)
    t.setheading(150)
    t.pendown()
    t.forward(arm_length)
    left_hand_x = t.xcor()
    left_hand_y = t.ycor()
    draw_hand(t, left_hand_x, left_hand_y, 150, scale)
    
    # Right arm and hand
    t.penup()
    t.goto(middle_radius, middle_center_y)
    t.setheading(30)
    t.pendown()
    t.forward(arm_length)
    right_hand_x = t.xcor()
    right_hand_y = t.ycor()
    draw_hand(t, right_hand_x, right_hand_y, 30, scale)
    
    # Draw speech bubble
    draw_speech_bubble(t, 80, 190, "Merry Christmas!", scale)
    
    # Hide turtle
    t.hideturtle()
    
def main():
    # Create screen
    screen = turtle.Screen()
    screen.title("Festive Snowman")
    
    # Draw snowman with different scales
    draw_snowman(scale=2)  # Normal size
    
    screen.exitonclick()

if __name__ == "__main__":
    main()