# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:45:42 2019

@author: E19SOE814
"""
'''
The process is in s0 90% of the time and it can
 move to s1 the remaining 10% of the time. 
When the process is in state s1 it will remain 
there 50% of the time. Given this data we
can create a Transition Matrix T as follow:
    
    
Let’s suppose we have to guess were the process 
will be after 3 steps and after 50 steps. 
How can we do it? We are interested in chains 
that have a finite number of states and are 
time-homogeneous meaning that the transition matrix
does not change over time.Given these assumptions 
we can compute the k-step transition probability as 
the k-th power of the transition matrix



# =============================================================================
# Markov chain of three state s0, s1, s2. Calculation of Transition probability Matrix after given interations. 
# =============================================================================

'''
import numpy as np

#Declaring the Transition Matrix T
T = np.array([[0.60, 0.10, 0.30 ],
              [0.10, 0.60, 0.30 ],
              [0.30, 0.10, 0.60]])

#Obtaining T after 3 steps
T_3 = np.linalg.matrix_power(T, 3)

T_7 = np.linalg.matrix_power(T, 7)
#Obtaining T after 50 steps
T_50 = np.linalg.matrix_power(T, 50)
#Obtaining T after 100 steps
T_100 = np.linalg.matrix_power(T, 100)


#Printing the matrices
print("T: \n" + str(T))

print("\n\nT_3:\n" + str(T_3))

print("\n\nT_7:\n" + str(T_7))

print("\n\nT_50: \n" + str(T_50))

print("\n\nT_100: \n" + str(T_100))