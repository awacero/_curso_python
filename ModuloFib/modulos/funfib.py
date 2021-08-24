# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:25:48 2021

@author: Juan Carlos
"""
def fibon(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        """c=a+b
        a=b
        b=c"""
        a, b = b, a+b
    #print()
#fibon(8) 