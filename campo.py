# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:05:16 2019

@author: Ariadna
"""

from slope_modificar_modulox import slope as slopex
from slope_modificar_moduloy import slope as slopey

def campo (X,Y,xo,yo,q1,q2):
    U=slopex(X,Y,q1,q2,xo,yo)
    V=slopey(X,Y,q1,q2,xo,yo)
    return (U,V)