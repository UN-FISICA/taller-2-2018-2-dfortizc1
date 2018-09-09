#!/usr/bin/python
# -*- coding: -utf8 -*-

from turtle import *
from math import *

setup(640,480,0,0)
title("Ejercicio2")

def ir(x,y): #Esta función manda, sin rayar, a la tortuga a una posición
    penup()
    goto(x,y)
    pendown()

def poligono2(x,n2,l2,teta2): #Forma un polígono de m lados con longitudes 2a
    while(n2<p2):
        forward(-2*x)
        left(teta2)
        n2+=1

def poligono1(x,n1,l1): #Forma un lado del cuadrado exterior con longitud 2a
    while(n1<l1):
        left(90*n1)        
        forward(-2*x)
        n1+=1

l2=input("Número de lados del polígono: ")

l1=4;  n1=0;  xy1=-100;      
p2=int(l2);  teta2=360/p2;  beta2=(p2-2)*180/p2;   xy2=-30;  
r2=2*xy2*abs(sin(radians(beta2/2))/sin(radians(teta2)));
h2=r2*abs(sin(radians(beta2/2)))  

ir(xy1,xy1)
while(n1<l1):
    ir(xcor()+xy2,ycor()+h2)
    right(heading())
    n2=0
    poligono2(xy2,n2,l2,teta2)
    ir(xcor()-xy2,ycor()-h2)
    #Si se desea ver el cuadrado grande, basta con comentar el 'penup()' que aparece a continuación.
    penup()
    poligono1(xy1,n1,1+n1)
    n1+=1

exitonclick()
