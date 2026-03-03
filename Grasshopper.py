import turtle

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
t.write("Grasshopper(Pass)", align="center", font=("Arial", 32, "bold"))


#Z Receiver
t.penup()
t.goto(0,-160)
t.pendown()
t.circle(20)

t.penup()
t.goto(2, -150)    
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
t.goto(250,0)
t.pendown()
t.circle(20)

t.penup()
t.goto(252, 10)    
t.write("Y", align="center", font=("Arial", 20))


#Center
t.penup()
t.goto(0,0)
t.pendown()
t.circle(20)


#X Receiver
t.penup()
t.goto(-250,0)
t.pendown()
t.circle(20)

t.penup()
t.goto(-248, 10)    
t.write("X", align="center", font=("Arial", 20))

t.hideturtle()
screen.update()    

t.speed(1)           # Set a visible animation speed
screen.tracer(1)  

#Quarterback Route
t.penup()
draw_quadratic_curve((20,-60),(70,-105),(170,-60))
t.pendown()

#Y Receiver Route
t.penup()
t.goto(250,40)
t.pendown()
x_points = [(250, 80),(250,300)]

for x, y in x_points:
    t.goto(x, y)

#X Receiver Path
t.penup()
t.goto(-250,40)
t.pendown()
x_points = [(-250, 80),(-150,130)]

for x, y in x_points:
    t.goto(x, y)

#Z Receiver Path
t.penup()
draw_quadratic_curve((0,-120),(-20,-60),(-150,-60))
t.pendown()

#X Receiver Path
t.penup()
t.goto(0,40)
t.pendown()
x_points = [(0, 80),(100,130)]

for x, y in x_points:
    t.goto(x, y)


turtle.done()
