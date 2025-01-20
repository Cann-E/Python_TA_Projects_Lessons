from turtle import *



def square(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)
    
def triangle(t,size):
    for i in range(3):
        t.forward(size)
        t.left(120)
    
def hexagon(t,size):
    for i in range(6):
        t.forward(size)
        t.right(60)

def octagon(t,size):
    for i in range(8):
        t.forward(size)
        t.right(45)        

