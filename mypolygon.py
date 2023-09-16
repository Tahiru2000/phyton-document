import turtle
bob =turtle.Turtle()
import math
#print(bob)
#turtle.mainloop()
#bob.fd(100)
#bob.lt(10)
#bob.fd(100)
#def square(t,length):
    #for i in range(4):
     #t.fd(length)
     #t.lt(90)
#square(bob,100)

def polygon(t,n,length):
    angle=360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob,7,70)


def circle(t,r):
    circumference=2*math.pi*r
    n=50
    length=circumference/n 
    polygon(t,n,length)

def circle(r,t):
    circumference=2*math.pi*r
    n= int(circumference/3)+3
    length=circumference/n
circle( bob t,r)

def arc(t,r,angle):
    arc_length= 2*math.pi*r*angle/360
    n= int(arc_length/3)+1
    step_length= arc_length/n
    step_angle= angle/n
    for i in range (n):
        t.fd(step_length)
        t.lt(step_angle)
    arc(t,r,angle)