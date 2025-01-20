from turtle import *

screen=Screen()
screen.bgcolor("black")

t1=Turtle()
t1.color("red")

def square(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)
    
    
def triangle(t,size):
    for i in range(3):
        t.forward(size)
        t.left(120)


response_1=input("What Kinda Shape Would you like to draw: ").lower()

if response_1=="square":
    square(t1,75)
elif response_1=="triangle":
    triangle(t1,45)
else:
    print("Not Created yet!")



done()
