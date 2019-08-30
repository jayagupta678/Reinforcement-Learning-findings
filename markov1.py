# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:42:19 2019

# =============================================================================
# @author: E19SOE814, https://mpatacchiola.github.io/blog/2016/12/09/dissecting-reinforcement-learning.html
# =============================================================================

# =============================================================================
# Markov chain of two state s0, s1, Calculation of Transition probability Matrix after given interations. 
# =============================================================================

"""

import numpy as np

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
print("T: " + str(T))
print("T_3: " + str(T_3))
print("T_7: " + str(T_7))
print("T_50: " + str(T_50))
print("T_100: " + str(T_100))
