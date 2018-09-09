from turtle import *
from math import *

setup(640,480,0,0)
title("Ejercicio4")

def ir(x,y): #Esta función manda, sin rayar, a la tortuga a una posición
    penup()
    goto(x,y)
    pendown()

def poligono2(x,n2,p2,teta2): #Forma un polígono de m lados con longitudes 2a
    while(n2<p2):
        forward(-2*x)
        left(teta2)
        n2+=1

l2=input("Número de lados del polígono: ")
l1=input("Número de filas de la pirámide: ")

y0=200   
n1=0;   p1=int(l1); 
xy2=-30;   p2=int(l2);  teta2=360/p2;  beta2=(p2-2)*180/p2;     
r2=2*xy2*abs(sin(radians(beta2/2))/sin(radians(teta2)));  
deltay0=2.2*r2

ir(0,y0)
while(n1<p1):
    n3=0
    while(n3<n1+1):
        ir(xcor()+xy2,ycor()+r2)
        right(heading())
        n2=0
        poligono2(xy2,n2,p2,teta2)
        ir(xcor()-xy2,ycor()-r2)
        if n3!=n1:
            penup()
            forward(2*r2)
        n3+=1
    penup()
    goto(0,ycor())
    right(-90)
    forward(deltay0)
    right(-90)
    forward((n1*r2)+r2)
    n1+=1
