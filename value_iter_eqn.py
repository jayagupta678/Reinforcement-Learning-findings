# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:35:53 2019

@author: E19SOE814

one way to find optimal policy matrix is value iteration algorithm
"""

import numpy as np

def return_state_utility(s, v, T, u, reward, gamma):
    """Return the state utility.

    @param v the state vector
    @param T transition matrix
    @param u utility vector
    @param reward for that state
    @param gamma discount factor
    @return the utility of the state
    """
    action_array = np.zeros(4)
    for action in range(0, 4):
        action_array[action] = np.sum(np.multiply(u, np.dot(v, T[:,:,action])))
        print("action_array",action_array)
        #print("Hello stackoverflow!", file=open("output.txt", "a"))
    print("state {0} utility : {1}".format(s, reward + gamma * np.max(action_array)), file=open("state_val.txt", "a"))
    return reward + gamma * np.max(action_array)

#def main():
#Change as you want
tot_states = 12
gamma = 0.999 #Discount factor
iteration = 0 #Iteration counter
epsilon = 0.01 #Stopping criteria small value

#List containing the data for each iteation
graph_list = list()

#Transition matrix loaded from file (It is too big to write here)
T = np.load('E:\Jaya\Reinforcement Learning\Cleaning bot\T.npy')

#Reward vector
r = np.array([-0.04, -0.04, -0.04,  +1.0,
              -0.04,   0.0, -0.04,  -1.0,
              -0.04, -0.04, -0.04, -0.04])    

#Utility vectors
u = np.array([0.0, 0.0, 0.0,  0.0,
               0.0, 0.0, 0.0,  0.0,
               0.0, 0.0, 0.0,  0.0])
u1 = np.array([0.0, 0.0, 0.0,  0.0,
                0.0, 0.0, 0.0,  0.0,
                0.0, 0.0, 0.0,  0.0])

while True:
    delta = 0
    u = u1.copy()
    iteration += 1
    graph_list.append(u)
    for s in range(tot_states):
        reward = r[s]
        v = np.zeros((1,tot_states))
        v[0,s] = 1.0
        u1[s] = return_state_utility(s, v, T, u, reward, gamma)
        delta = max(delta, np.abs(u1[s] - u[s])) #Stopping criteria       
    if delta < epsilon * (1 - gamma) / gamma:
            print("=================== FINAL RESULT ==================")
            print("Iterations: " + str(iteration))
            print("Delta: " + str(delta))
            print("Gamma: " + str(gamma))
            print("Epsilon: " + str(epsilon))
            print("===================================================")
            print(u[0:4])
            print(u[4:8])
            print(u[8:12])
            print("===================================================")
            break

#if __name__ == "__main__":
#    main()
