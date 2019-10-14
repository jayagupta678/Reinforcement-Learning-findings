
'''
import gym
env = gym.make('SpaceInvaders-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(1000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()

from time import sleep

for i in range(10):
    print i
    sleep(0.5)   
'''
import gym
from time import sleep
env = gym.make('BipedalWalker-v2')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        #sleep(.25)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()

'''
import gym
env = gym.make('SpaceInvaders-v0')
env.reset()
env.render()


import gym
env = gym.make('FrozenLake-v0')
env.reset()
env.render()



import gym
env = gym.make('Pendulum-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()
'''