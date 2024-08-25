# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:40:39 2024

@author: ASUS
"""
N = int(input("nhap so nguyen duong co 2 chu so: "))
if 10<= N <=99:
    print("chu so thu nhat ", N//10)
    print("chu so thu hai ", N%10)
    S= N//10 + N%10
    print(" tong la: ", S)
    