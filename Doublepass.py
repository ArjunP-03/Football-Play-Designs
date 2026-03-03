import turtle

def draw_oval(radius):
    """
    Draws a horizontal oval using a series of partial circles.
    The 'radius' parameter controls the overall size.
    """
    turtle.right(45) # Tilt the starting direction for a horizontal oval
    for _ in range(2):
        turtle.circle(radius, 90) # Long curved part (90 degrees)
        turtle.circle(radius / 2, 90) # Short curved part (90 degrees)

def draw_quadratic_curve(p0, p1, p2, steps=20):
    """
    Draws a smooth curve through three points using linear interpolation.
    p0, p1, p2: tuples (x, y)
    steps: more steps = smoother curve
    """
    t.penup()
    t.goto(p0)
    t.pendown()

    for i in range(steps + 1):
        t_val = i / steps
        # Quadratic Bezier formula
        x = (1 - t_val)**2 * p0[0] + 2 * (1 - t_val) * t_val * p1[0] + t_val**2 * p2[0]
        y = (1 - t_val)**2 * p0[1] + 2 * (1 - t_val) * t_val * p1[1] + t_val**2 * p2[1]
        t.goto(x, y)


screen = turtle.Screen()
screen.tracer(0)   

screen.bgpic("Field.png")


t = turtle.Turtle()

t.penup()
t.goto(0,300)
t.write("Double Pass", align="center", font=("Arial", 32, "bold"))


#Z Receiver
t.penup()
t.goto(100,0)
t.pendown()
t.circle(20)

t.penup()
t.goto(102, 10)    
t.write("Z", align="center", font=("Arial", 20))

#Quarterback
t.penup()
t.goto(-20,-35)
t.pendown()
for _ in range(4):
    t.forward(40)
    t.right(90)

#Y Receiver 
t.penup()
t.goto(230,0)
t.pendown()
t.circle(20)

t.penup()
t.goto(232, 10)    
t.write("Y", align="center", font=("Arial", 20))


#Center
t.penup()
t.goto(0,0)
t.pendown()
t.circle(20)


#X Receiver
t.penup()
t.goto(165,0)
t.pendown()
t.circle(20)

t.penup()
t.goto(167, 10)    
t.write("X", align="center", font=("Arial", 20))

t.hideturtle()
screen.update()    

t.speed(1)           # Set a visible animation speed
screen.tracer(1)  


#Z Receiver Path(part1)
t.penup()
draw_quadratic_curve((100,0),(50,-75),(40,-100))
t.pendown()

#Z receives football
t.penup()
draw_quadratic_curve((40,-120),(50,-100),(40,-80))
t.pendown()

#Z receives football
t.penup()
draw_quadratic_curve((40,-80),(30,-100),(40,-120))
t.pendown()


#Z Receiver Path(part1)
t.penup()
draw_quadratic_curve((40,-100),(50,-99),(200,-90))
t.pendown()



#Quarterback Route
t.penup()
draw_quadratic_curve((-0,-75),(0,-150),(-250,-10))
t.pendown()

#X Receiver Path
t.penup()
t.goto(165,40)
t.pendown()
x_points = [(165, 80),(165,300)]

for x, y in x_points:
    t.goto(x, y)

#Y Receiver Route
t.penup()
t.goto(230,40)
t.pendown()
x_points = [(230, 250),(270,220)]

for x, y in x_points:
    t.goto(x, y)

#Center Receiver Path
t.penup()
t.goto(0,40)
t.pendown()
x_points = [(0, 120),(70,120)]

for x, y in x_points:
    t.goto(x, y)


turtle.done()
