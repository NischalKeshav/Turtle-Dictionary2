import turtle 

import colorgram
turtle.colormode(255)
screen = turtle.Screen()
Turtle = turtle.Turtle()
Turtle.shape("turtle")
screen.screensize(1400,1400)
from random import *
import random
list = ["red","green","blue","brown","orange","pink","red","green"]
#Turtle.width(5)
Turtle.speed("fastest")
def shaper(list):  
  random.shuffle(list)
  for i in range(3,10):
    Turtle.color(list[i-3])
    for  i2 in range(i):
      Turtle.forward(100)
      Turtle.right(360/i)
def random_path(list):
  while 1:  
    x=random.randrange(-360,360,90)
    Turtle.color(random.choice(list))
    Turtle.forward(15)
    Turtle.right(x)

def random_path2():
  while 1:  
    x=random.randrange(-360,360,90)
    Turtle.color(randrange(0,255),randrange(0,255),randrange(0,255))
    Turtle.forward(15)
    Turtle.right(x)
def spirograph(radius,rote=36):
  rotate= 360/rote
  for x in range(rote):
    Turtle.color(randrange(0,255),randrange(0,255),randrange(0,255))
    Turtle.circle(radius)
    Turtle.right(rotate)
spirograph(50)