# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:12:01 2024

@author: ASUS
"""

time = input("nhap vao gio, phut va giay (theo dang hh:mm:ss): ")
hh, mm, ss = map(int, time. split(":"))
if 0 <= hh < 24 and 0<= mm < 60 and 0<= ss <60:
    SS = hh*3600 + mm*60 + ss
    print(" Tong so giay la ", SS)
else:
    print("thoi gian khong hop le")
    