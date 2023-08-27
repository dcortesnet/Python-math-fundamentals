import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=300, height=300, startx=0, starty=0)

radius = 50

t = turtle.Turtle()
t.circle(radius)

screen.mainloop()