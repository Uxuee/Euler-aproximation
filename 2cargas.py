# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:48:54 2019

@author: Ariadna
"""

import numpy as np
import matplotlib.pyplot as plt
from puntos4cargas import puntos
from nuevoeulerxyprob import euler_aprox
from campo import campo

n=int(input("how many rays?#for the moment just pairs pls: "))
r=1
#int(input("radii: "))
h=float(input("\nWhat h?: "))
q1=int(input("+1 or -1 for charge 1 pls:"))
q2=int(input("+1 or -1 for charge 2 pls:"))
x0=float(input("put the place of the charge pls: "))
y0=float(input("put the yplace of the charge pls: "))


(A,B)=puntos(n,r,x0,y0)

for u in range (4*n+4):
    xo=A[u]
    yo=B[u]
    euler_aprox(xo,yo,h,q1,q2,x0,y0)

plt.xlim(-40, 40)
plt.ylim(-40, 40)   


#la otra cosa
x=np.linspace(-40,40,80)
y=np.linspace(-40,40,80)
X,Y= np.meshgrid(x,y)

(U,V)=campo(X,Y,20,20,1,-1)

   
plt.streamplot(X,Y,U,V) 
plt.show()


