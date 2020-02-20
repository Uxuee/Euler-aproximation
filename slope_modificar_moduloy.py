# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:05:56 2020

@author: Ariadna
"""
from modulo import modulo

def slope(xi,yi,q1,q2,x0,y0):
    r1=((xi-x0)**2+(yi-y0)**2)**0.5
    r2=((xi+x0)**2+(yi+y0)**2)**0.5
    
    Ex=q1*(xi-x0)/(r1**3)+q2*(xi+x0)/(r2**3)
    Ey=q1*(yi-y0)/(r1**3)+q2*(yi+y0)/(r2**3)
    E=modulo(Ex,Ey)
    return Ex/E