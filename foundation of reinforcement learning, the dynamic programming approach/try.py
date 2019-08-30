# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:04:52 2019

@author: E19SOE814
"""
 #action_array[action] = np.sum(np.multiply(u, np.dot(v, T[:,:,action])))
import numpy as np
v = np.zeros((1,12))
v[0,0] = 1.0

u = np.array([0.0, 0.0, 0.0,  0.0,
               0.0, 0.0, 0.0,  0.0,
               0.0, 0.0, 0.0,  0.0])
T = np.load('E:\Jaya\Reinforcement Learning\Cleaning bot\T.npy')
action_array = np.zeros(4)
val = []
for action in range(0, 4):
    k = np.dot(v, T[:,:,action])
    print("probability of being in a specific state after 1 iterations:\n",k)
    l = np.sum(np.multiply(u, k))
    print("utility of an state by performing each action(up, left, down, right):\n", l)
    