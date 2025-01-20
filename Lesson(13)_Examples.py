from turtle import *

screen = Screen()
screen.bgcolor("black")

red_turtle=Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.width(5)
red_turtle.speed=1

green_turtle=Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")
green_turtle.width(5)
green_turtle.speed=1

blue_turtle=Turtle()
blue_turtle.color("blue")
blue_turtle.shape("turtle")
blue_turtle.width(5)
blue_turtle.speed=1

# red_turtle.forward(200)
# red_turtle.right(45)
# red_turtle.forward(200)
# red_turtle.right(45)
# red_turtle.forward(200)
# red_turtle.right(45)
# red_turtle.forward(200)
# red_turtle.right(45)
# red_turtle.forward(200)
# red_turtle.right(45)
# red_turtle.forward(200)
# red_turtle.right(45)
# red_turtle.forward(200)
# red_turtle.right(45)
# red_turtle.forward(200)

# done()

##########################

# start_position=red_turtle.pos()

# while True:
#     red_turtle.forward(200)
#     red_turtle.right(45)
#     if red_turtle.distance(start_position)<1:
#         break

# for i in range(6):
#     red_turtle.forward(200)
#     red_turtle.right(45)




############################

red_turtle.begin_fill()
red_turtle.left(45)
red_turtle.forward(200)
print(red_turtle.pos())
red_turtle.right(90)
red_turtle.forward(200)
red_turtle.right(135)
red_turtle.forward(280)
red_turtle.end_fill()

green_turtle.penup()
green_turtle.goto(141.42,141.42)
green_turtle.left(90)

green_turtle.pendown()
green_turtle.begin_fill()
green_turtle.left(90)
green_turtle.forward(100)
green_turtle.right(135)
green_turtle.forward(150)
print(green_turtle.pos())
green_turtle.right(90)
green_turtle.forward(150)
green_turtle.right(135)
green_turtle.forward(120)
green_turtle.end_fill()

blue_turtle.penup()
blue_turtle.goto(147.49,247.49)
blue_turtle.left(180)

blue_turtle.pendown()
blue_turtle.begin_fill()
blue_turtle.forward(100)
blue_turtle.right(135)
blue_turtle.forward(150)
print(blue_turtle.pos())
blue_turtle.right(90)
blue_turtle.forward(150)
blue_turtle.right(135)
blue_turtle.forward(120)
blue_turtle.end_fill()
done()