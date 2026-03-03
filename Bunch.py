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
t.write("Bunch", align="center", font=("Arial", 32, "bold"))


#Z Receiver
t.penup()
t.goto(50,0)
t.pendown()
t.circle(20)

t.penup()
t.goto(52, 10)    
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
t.goto(100,0)
t.pendown()
t.circle(20)

t.penup()
t.goto(102, 10)    
t.write("Y", align="center", font=("Arial", 20))


#Center
t.penup()
t.goto(0,0)
t.pendown()
t.circle(20)


#X Receiver
t.penup()
t.goto(-50,0)
t.pendown()
t.circle(20)

t.penup()
t.goto(-48, 10)    
t.write("X", align="center", font=("Arial", 20))

t.hideturtle()
screen.update()    

t.speed(1)           # Set a visible animation speed
screen.tracer(1)  


#Y Receiver Route
t.penup()
t.goto(100,40)
t.pendown()
x_points = [(100, 250),(150,300)]

for x, y in x_points:
    t.goto(x, y)
    
#Z Receiver Path
t.penup()
t.goto(50,40)
t.pendown()
x_points = [(50, 100),(50,300)]

for x, y in x_points:
    t.goto(x, y)


#X Receiver Route
t.penup()
t.goto(-50,40)
t.pendown()
x_points = [(-50, 150),(-150,150)]

for x, y in x_points:
    t.goto(x, y)

#Center Route
t.penup()
t.goto(0,40)
t.pendown()
x_points = [(0, 200),(45,160)]

for x, y in x_points:
    t.goto(x, y)


turtle.done()
