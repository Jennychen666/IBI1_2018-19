# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:40:00 2019

@author: admin
"""

a=123
b=123123
c=b/7
d=c/11
e=int(d/13)
print('e is',e)
if e==a:
    print('e is equal to a')
elif e<a:
    print('e is smaller than a')
else:
    print('e is bigger than a')  
X=True
Y=False
if (X and not Y) or (Y and not X):
    print("Z is True")
if X!=Y:
    print("W is True")
if (X and not Y) or (Y and not X) == X!=Y:
     print("Z and W are the same")
else:
     print("Z and W are not the same")
    