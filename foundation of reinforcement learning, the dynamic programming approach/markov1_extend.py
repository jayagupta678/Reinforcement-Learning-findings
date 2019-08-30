# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:57:21 2019

@author: E19SOE814
"""

'''
The process is in s0 90% of the time and it can
 move to s1 the remaining 10% of the time. 
When the process is in state s1 it will remain 
there 50% of the time. Given this data we
can create a Transition Matrix T as follow:
    
 the probability of being in a specific 
 state after k iterations, given that
 the initial distribution which represent
 the state of the system at k=0 is 
 v = (1, 0),
 
 Our system is composed of two states and
 we can model the initial distribution as
 a vector with two elements, the first element
 of the vector represents the probability of
 staying in the state s0 and the second element
 the probability of staying in state s1. Let’s
 suppose that we start from s0, the vector v
 representing the initial distribution will have this form 
 
 
# =============================================================================
# Markov chain of two state s0, s1, Calculation of system state after given interations. 
# =============================================================================

'''

import numpy as np


#Declaring the initial distribution v  = np.array([[1,0]])
v = [.7,.3]
#Declaring the Transition Matrix T
T = np.array([[0.90, 0.10],
              [0.50, 0.50]])

#Obtaining T after 3 steps
T_3 = np.linalg.matrix_power(T, 3)

T_7 = np.linalg.matrix_power(T, 7)
#Obtaining T after 50 steps
T_50 = np.linalg.matrix_power(T, 50)
#Obtaining T after 100 steps
T_100 = np.linalg.matrix_power(T, 100)


#Printing the matrices
#Printing the matrices
print("T: \n" + str(np.dot(T, v)))

print("\n\nT_3:\n" + str(np.dot(T_3, v)))

print("\n\nT_7:\n" + str(np.dot(T_7, v)))

print("\n\nT_50: \n" + str(np.dot(T_50, v)))

print("\n\nT_100: \n" + str(np.dot(T_100, v)))