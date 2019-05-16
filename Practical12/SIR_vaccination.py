# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:28:55 2019

@author: admin
"""

import numpy as np 
import matplotlib.pyplot as plt
P=0
N=10000 #population
#rate that depends on an infection probability upon contact 
beta=0.3
# recover (R) with recovery probability γ 
gamma=0.05
plt.figure(figsize =(6,4) , dpi=150)     #put at the beginning, or there will be a blank graph.  
#plot the legend 
for i in range(1,11):
    #V should be interprted as an integer instead of 'float' objects.(or error occurs)
    V=int(N*P*0.01)
    p=str(P)+'%'
    P=P+10
    I=1 #infected 
    R=0 #recovered
    S=N-I-R-V 
    #set arrays to add the values
    susceptible=[S]
    infected=[1]
    recovered=[0]
    #loop over 1000 times
    for i in range(1,1001):
      #randomly choose the people becoming infected
      #randomly choose the recovered people 
      r1=np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N])
      s1=sum(r1)
      S=S-s1
      I=I+s1
      susceptible.append(S)
      r2=np.random.choice(range(2),I,p=[1-gamma,gamma])
      s2=sum(r2)
      I=I-s2
      R=R+s2 
      infected.append(I)
      recovered.append(R)
    #construct the plot, the colors of legend correspond with the colors of infected plot
    plt.plot(infected,label=p)
    plt.xlabel('time')
    plt.ylabel('number of people')
    plt.title('SIR model with different vaccination rates')
    plt.legend()
    #save to png
    plt.savefig('C:/Users/admin/Desktop/IBI/IBI1_2018-19/Practical12/SIR_vaccination.png',type='png')

