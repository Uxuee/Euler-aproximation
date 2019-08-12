# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 23:03:52 2019

@author: Ariadna
"""
import matplotlib.pyplot as plt
from slope_modificar_modulox import slope as slopex
from slope_modificar_moduloy import slope as slopey
from modulo import modulo

def euler_aprox(xo,yo,h,q1,q2,x0,y0):
    #listas que tienen todos los puntos a plotear
    X=[xo,]
    Y=[yo,]


    for n in range(600):
        #posiciónes actuales
        xi=X[n]
        yi=Y[n]
        #cálculo de la pendiente inmediata
        fa=slopex(xi,yi,q1,q2,x0,y0)
        fb=slopey(xi,yi,q1,q2,x0,y0)
        #normalizando
        m=modulo(fa,fb)
        f1=fa/m
        f2=fb/m
        plt.xlim(-40, 40)
        plt.ylim(-40, 40)


        #recolectando puntos en las listas
        X.append(X[n]+f1*h)
        Y.append(Y[n]+f2*h)
        plt.plot(X,Y, color='blue')

            
  