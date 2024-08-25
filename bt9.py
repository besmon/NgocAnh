# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:04:55 2024

@author: ASUS
"""
import math
a=float(input("Nhap a: "))
b=float(input("nhap b: "))

x=math.sqrt(a)-math.sqrt(b)
y=a**(1/4)-b**(1/4)
z=math.sqrt(a) + ((a*b)**(1/4))
w=(a)**(1/4) + (b)**(1/4)
k= (x/y) - (z/w)
print("Ket qua: ", k)