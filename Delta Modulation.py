# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:12:52 2021

@author: haygr
"""

import numpy as np
import matplotlib.pyplot as plt

#DM Transmitter
def delta(x,d):
    e = eq = mq = np.zeros(len(x))
    for i in range(len(x)):
        if i == 0:
            e[i] = x[i]
            eq[i] = d*np.sign(e[i])
            mq[i] = eq[i]
        else:
            e[i] = x[i] - mq[i-1]
            eq[i] = d*np.sign(e[i])
            mq[i] = eq[i] + mq[i-1]
    
    return mq

def a_delta(x,d):
    e = eq = mq = np.zeros(len(x))
    K = 1.5
    D_o = d
    for i in range(len(x)):
        if i == 0:
            e[i] = x[i]
            eq[i] = d*np.sign(e[i])
            mq[i] = eq[i]
        else:
            print(f'K={K}, eq[i-1] = {eq[i-1]},eq[i]={eq[i]}')
            D = D_o * np.power(K,(D_o*np.sign(e[i])*eq[i-1]))
            print('D:',D)
            e[i] = x[i] - mq[i-1]
            D_o = D
            mq[i] = eq[i] + mq[i-1]
            
    
    return mq

f1 = 500 # Frequency 1
f2 = 1000 # Frequency 2
f3 = 1500 # Frequency 3
fm = max(f1,f2,f3)
fs = 10*fm

t = np.arange(0,1,1/fs)

x = [(np.sin((2*np.pi*f1/fs)*t))+(2*(np.sin((2*np.pi*f2/(fs))*t)))+(3*(np.sin((2*np.pi*f3/fs)*t))) for t in range(0,100)]

#x = [1 for i in range(100)]
am = max(x)

d = (2*np.pi*am*(fm/fs)) # Step Size

#d = 0.05

X = delta(x,d)

X_1 = a_delta(x, d)

plt.figure(1)
plt.title('Quantized Signal using Delta Modulation')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.plot(t[:100],x[:100])
plt.step(t[:100],X[:100])

plt.figure(2)
plt.title('Quantized Signal using Adaptive Delta Modulation')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.plot(t[:100],x[:100])
plt.step(t[:100],X_1[:100])


    