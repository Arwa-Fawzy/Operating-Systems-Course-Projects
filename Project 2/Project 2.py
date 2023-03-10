#import necessary packages
import turtle
from multiprocessing import Process
    
# Initializing the two windows of turtle 
#one for circle and another for rectangle

t1=turtle.Turtle()
t2=turtle.Turtle()

def circle():
  
  # moving in a 360 degree direction
  i=0
  while i < 360:
    #delay the speed 
    turtle.delay(10)
    t1.forward(1)
    t1.left(1)
    i+=1

# intializing the length=l and width=w
l=80
w=40
def rectangle():
    #delay the speed 
    turtle.delay(200)
    # drawing first side
    t2.forward(l) # Forward turtle by l units
    t2.left(90) # Turn turtle by 90 degree

    # drawing second side
    t2.forward(w) # Forward turtle by w units
    t2.left(90) # Turn turtle by 90 degree

    # drawing third side
    t2.forward(l) # Forward turtle by l units
    t2.left(90) # Turn turtle by 90 degree

    # drawing fourth side
    t2.forward(w) # Forward turtle by w units
    t2.left(90) # Turn turtle by 90 degree

#calling the windows 
if __name__ == '__main__':
  p1 = Process(target=circle)
  p1.start()
  p2 = Process(target=rectangle)
  p2.start()
  p1.join()
  p2.join()

