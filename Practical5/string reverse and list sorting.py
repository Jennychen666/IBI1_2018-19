# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:03:34 2019

@author: admin
"""

sequence="but soft what light yonder window breaks"
sequence=sequence[ ::-1]
sequence=sequence.split(" ")

sequence.sort()
sequence.reverse()
print(sequence)
