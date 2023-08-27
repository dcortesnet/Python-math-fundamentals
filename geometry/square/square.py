import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=300, height=300, startx=0, starty=0)

side_length = 100

t = turtle.Turtle()
t.forward(side_length) 
t.left(90) # turn 90 angle left
t.forward(side_length)
t.left(90) # turn 90 angle left
t.forward(side_length)
t.left(90) # turn 90 angle left
t.forward(side_length)

screen.mainloop()