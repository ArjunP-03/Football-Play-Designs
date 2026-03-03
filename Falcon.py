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
t.write("Falcon", align="center", font=("Arial", 32, "bold"))


#Z Receiver
t.penup()
t.goto(230,-20)
t.pendown()
t.circle(20)

t.penup()
t.goto(232, -10)    
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
t.goto(150,0)
t.pendown()
t.circle(20)

t.penup()
t.goto(152, 10)    
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
draw_quadratic_curve((232,-20),(230,-50),(152,-15))
t.pendown()


#Y Receiver Route
t.penup()
draw_quadratic_curve((169,15),(232, 25),(232,220))
t.pendown()

#X Receiver Route
t.penup()
t.goto(-250,40)
t.pendown()
x_points = [(-250, 200),(-150,200)]

for x, y in x_points:
    t.goto(x, y)

#Center Route
t.penup()
draw_quadratic_curve((-13,4),(-20, -30),(-100,-31))
t.pendown()


turtle.done()
