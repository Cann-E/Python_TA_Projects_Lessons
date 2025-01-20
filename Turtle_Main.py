from TurtleCan import *


screen=Screen()
screen.bgcolor("black")


t1=Turtle()
t1.color("red")
t1.shape("turtle")
t1.penup()
t1.goto(200,-400)
t1.pendown()

t2=Turtle()
t2.color("green")
t2.shape("arrow")
t2.penup()
t2.goto(800,0)
t2.pendown()

t3=Turtle()
t3.color("orange")
t3.shape("circle")
t3.penup()
t3.goto(-200,400)
t3.pendown()

t4=Turtle()
t4.color("white")
t4.shape("square")
t4.penup()
t4.goto(-800,0)
t4.pendown()



system_=int(input("Welcome To Drawing Game:\n"
              "Press 1 To Start Drawing\n"
              "Press 2 To End Drawing\n"
              ": "))

while system_!= "2":
    response_=input("Please Pick Your Pencil(Turtle,Arrow,Circle,Square): ").lower()
    response_1=input("What Would you like to draw(Square,Triangle,Hexagon,Octagon?: ").lower()
    response_2=int(input("How big would you like to draw: "))
    if response_1=="square" and response_=="turtle":
        print("Here Is Your Square:!!")
        square(t1,response_2)
    elif response_1=="square" and response_=="arrow":
        print("Here Is Your Square:!!")
        square(t2,response_2)
    elif response_1=="square" and response_=="circle":
        print("Here Is Your Square:!!")
        square(t3,response_2)
    elif response_1=="square" and response_=="square":
        print("Here Is Your Square:!!")
        square(t4,response_2)
    elif response_1=="triangle" and response_=="turtle":
        print("Here Is Your Triangle:!!")
        triangle(t1,response_2)
    elif response_1=="triangle" and response_=="arrow":
        print("Here Is Your Triangle:!!")
        triangle(t2,response_2)
    elif response_1=="triangle" and response_=="circle":
        print("Here Is Your Triangle:!!")
        triangle(t3,response_2)
    elif response_1=="triangle" and response_=="square":
        print("Here Is Your Triangle:!!")
        triangle(t4,response_2)
    elif response_1=="hexagon" and response_=="turtle":
        print("Here Is Your hexagon:!!")
        hexagon(t1,response_2)
    elif response_1=="hexagon" and response_=="arrow":
        print("Here Is Your hexagon:!!")
        hexagon(t2,response_2)
    elif response_1=="hexagon" and response_=="circle":
        print("Here Is Your hexagon:!!")
        hexagon(t3,response_2)
    elif response_1=="hexagon" and response_=="square":
        print("Here Is Your hexagon:!!")
        hexagon(t4,response_2)    
    elif response_1=="octagon" and response_=="turtle":
        print("Here Is Your octagon:!!")
        octagon(t1,response_2)
    elif response_1=="octagon" and response_=="arrow":
        print("Here Is Your octagon:!!")
        octagon(t2,response_2)
    elif response_1=="octagon" and response_=="circle":
        print("Here Is Your octagon:!!")
        octagon(t3,response_2)
    elif response_1=="octagon" and response_=="square":
        print("Here Is Your octagon:!!")
        octagon(t4,response_2)
    system_=int(input("--------------\n"
              "Press 1 To Continue Drawing\n"
              "Press 2 To End Drawing\n"
              "---------- "))
    
print("THANK YOU FOR PLAYING!!!!!!")        

done() 