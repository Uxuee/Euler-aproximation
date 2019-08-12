# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:59:02 2019

@author: Ariadna
"""
import math

def puntos (n,r,x0,y0):
    m=360/n
    A=[]
    B=[]

    u=int((n/2)+1)
    #x0<0 donde x0 es la posición de la carga
        #y>0
    a=0+m
    for i in range(u-1):
        x=math.cos(a*math.pi/180)-x0
        y=(r**2-(x+x0)**2)**0.5
        a=a+m
        A.append(x)
        B.append(y)
        #y<0
    a=0+m
    for o in range(u-1):
        x=math.cos(a*math.pi/180)-x0
        y=-1*(r**2-(x+x0)**2)**0.5
        a=a+m
        A.append(x)
        B.append(y)
    #x0>0
        #y>0
    a=0
    for y in range(u-1):
        x=math.cos(a*math.pi/180)+x0
        y=(r**2-(x-x0)**2)**0.5
        a=a+m
        A.append(x)
        B.append(y)
        #y>0
    a=0
    for p in range(u-1):
        x=math.cos(a*math.pi/180)+x0
        y=-1*(r**2-(x-x0)**2)**0.5
        a=a+m
        A.append(x)
        B.append(y)
    #carga en el centro
    a=0
    for i in range(n):
        x=math.cos(a*math.pi/180)
        y=math.sin(a*math.pi/180)
        a=a+m
        A.append(x)
        B.append(y)
    #carga encima y0
    a=0
    for i in range(n):
        x=math.cos(a*math.pi/180)
        y=math.sin(a*math.pi/180)+y0
        a=a+m
        A.append(x)
        B.append(y)

 
    return(A,B)