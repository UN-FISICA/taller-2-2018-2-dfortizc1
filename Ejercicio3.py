from turtle import *
from math import *

setup(640,480,0,0)
title("Ejercicio3")

def ir(x,y): #Esta función manda, sin rayar, a la tortuga a una posición
    penup()
    goto(x,y)
    pendown()

def poligono2(x,n2,l2,teta2): #Forma un polígono de m lados con longitudes 2a
    while(n2<p2):
        forward(-2*x)
        left(teta2)
        n2+=1

def poligono1(x,n1,l1,beta1): #Ayuda a formar un polígono de m lados con longitudes 2a
    while(n1<l1):
        left((180-beta1)*n1)        
        forward(-2*x)
        n1+=1

l2=input("Número de lados del polígono: ")
l1=input("Número de lados del polígono de alineación: ")

n1=0;  
xy1=-100;  p1=int(l1);  teta1=360/p1;  beta1=(p1-2)*180/p1;
r1=2*xy1*abs(sin(radians(beta1/2))/sin(radians(teta1)));
h1=r1*abs(sin(radians(beta1/2)))   
xy2=-30;   p2=int(l2);  teta2=360/p2;  beta2=(p2-2)*180/p2;     
r2=2*xy2*abs(sin(radians(beta2/2))/sin(radians(teta2)));
h2=r2*abs(sin(radians(beta2/2)))  

ir(xy1,h1)
while(n1<p1):
    ir(xcor()+xy2,ycor()+h2)
    right(heading())
    n2=0
    poligono2(xy2,n2,l2,teta2)
    ir(xcor()-xy2,ycor()-h2)
    #Si se desea ver el polígono grande, basta con comentar el 'penup()' que aparece a continuación.
    penup()
    poligono1(xy1,n1,1+n1,beta1)
    n1+=1
