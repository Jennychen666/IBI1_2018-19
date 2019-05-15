# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:08:50 2019

@author: admin
"""

# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt
N=10000 #population
# rate that depends on an infection probability upon contact 
beta=0.3
# recover (R) with recovery probability γ 
gamma=0.05
infected=[1]
susceptible=[9999]
recovered=[0]
I=1 #infected 
R=0 #recovered 
S=9999 #susceptible

for i in range(1,1001):
  r1=np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N])
#L1数组总和为1显示感染
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
  
print("The present susceptible people:",S)
print("The present infected people:",I)
print("The present recovered people:",R)

plt.figure(figsize =(6,4) , dpi=150)
#put at the beginning, or there will be a blank graph.
plt.plot(infected)
plt.plot(susceptible)
plt.plot(recovered)
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR'+ ' '+'model')
plt.legend(labels=['infected','susceptible','recovered'],loc='upper right')

plt.savefig('C:/Users/admin/Desktop/IBI/IBI1_2018-19/week12/SIR_model.png',type='png')

