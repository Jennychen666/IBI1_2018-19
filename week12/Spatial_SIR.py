# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:17:13 2019

@author: admin
"""

import numpy as np 
import matplotlib . pyplot as plt
#population
# rate that depends on an infection probability upon contact 
beta=0.3
# recover (R) with recovery probability γ 
gamma=0.05
population = np. zeros ((100 , 100))
#0 for susceptible, 1 for infected, 2 for recovered
# find infected points   
outbreak = np.random. choice (range(100) ,2) 
population [outbreak [0] , outbreak[1]]=1
for n in range(0,101):
    infectedIndex = np.where(population==1)
# loop through all infected points
    for i in range(len(infectedIndex[0])):
       # get x, y coordinates for each point
       x = infectedIndex[0][i]
       y = infectedIndex[1][i]
        #for himself, g probability he recovered (=2)
       population[x,y] = np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
       for xNeighbour in range(x-1,x+2):
           for yNeighbour in range(y-1,y+2):
       # infect each neighbour with probability beta
       # infect all 8 neighbours (this is a bit finicky, is there a better way?):
             # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                   # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
                         #model at times 0, 10, 50, and 100
    if n in [0,10,50,100]:
     plt . figure (figsize =(6,4) , dpi=150) 
     plt . imshow(population, cmap='viridis' , interpolation='nearest')
# On this heat map, susceptible individuals are shown in dark purple, infected individuals in blue-green and recovered individuals in yellow.
