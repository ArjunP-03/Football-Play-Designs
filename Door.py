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
t.write("Door(Run Play)", align="center", font=("Arial", 32, "bold"))


#Z Receiver
t.penup()
t.goto(70,-100)
t.pendown()
t.circle(20)

t.penup()
t.goto(72, -90)    
t.write("Z", align="center", font=("Arial", 20))

#Quarterback
t.penup()
t.goto(-20,-65)
t.pendown()
for _ in range(4):
    t.forward(40)
    t.right(90)

#Y Receiver 
t.penup()
t.goto(-100,-105)
t.pendown()
t.circle(20)

t.penup()
t.goto(-98, -95)    
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

#Z Receiver Path
t.penup()
t.goto(50,-75)
t.pendown()
t.goto(-50,-25)


turtle.done()
