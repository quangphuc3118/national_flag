import turtle

bg = turtle.Screen()
bg.bgcolor("white")

fl = turtle.Turtle()
fl.shape("turtle")
fl.color("red")

fl.penup()
fl.goto(-300, -200)
fl.pendown()

fl.fillcolor("red")
fl.pencolor("red")
fl.begin_fill()

for _ in range(2):
    fl.forward(600)
    fl.left(90)
    fl.forward(400)
    fl.left(90)

fl.end_fill()

fl.fillcolor("yellow")
fl.pencolor("yellow")

fl.penup()
fl.goto(0,120)
fl.right(108)
fl.begin_fill()

for _ in range(5):
    fl.forward(87.18510336)
    fl.right(72)
    fl.forward(87.18510336)
    fl.left(144)

fl.end_fill()
fl.penup()
fl.goto(700,500)

bg.exitonclick()

# chúc mừng Quốc Khánh Nước CHXHCN Việt Nam

#QuangPhuc
## vào vd thả tim giúp mình nè <3