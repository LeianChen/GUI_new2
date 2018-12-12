#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__ 1.0.0

Basic agent-based modelling. Builds agents into a 2D plane represented by a
raster environment. Scrapes some web data and use it to initialise the model.
Agents have methods of move, eat, and share.

"""

import random

class Agent():
    
    def __init__(self, environment, agents, x, y):
        
        """
        Initialises the agent.
        Positional arguments:
            environment: the raster environment for all the agents to be shared
                        with each other.
            agents: a reference to all the agents in the environment.
            x: the x-axis coordinates.
            y: the y-axis coordinates.
        """
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.x = x #random.randint(0,299)
        self.y = y #random.randint(0,299)
        if (x == None):
            self._x = random.randint(0,99)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,99)
        else:
            self._y = y
    
    def move(self):
        """
        Moves an agent within the 100x100 environment framework in either
        x or y direction.
        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 99
        else:
            self.y = (self.y - 1) % 99

        if random.random() < 0.5:
            self.x = (self.x + 1) % 99
        else:
            self.x = (self.x - 1) % 99
    
    def eat(self):
        """
        Agents eat some of the environment. If their store is greater than 100,
        50% of it is returned back to the environment.
        """
        #If more than 10 get 10
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            #Store what is left
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        #print(str(self.store))
        if self.store > 100:
            self.environment[self.y][self.x] = self.environment[self.y][self.x] + 100
            self.store = 50


    def share_with_neighbours(self, neighbourhood):
        """
        Agents share their store with other agents.
        
        Positional argument:
            neighbourhood: agents share with others within the distance.
        """
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                
                #print('other store: '+ str(agent.store)) #check other agents' store
                #print('own store: '+ str(self.store)) #check self store
                
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))

                #print('other store: '+ str(agent.store))
                #print('own store: '+ str(self.store))
                #print('-------------------------------')
                #print("sharing " + str(dist) + " " + str(ave))
                # could try to remove the agent from agents list

    def distance_between(self, agent):
        """
        Calculate and return the distance between self and agent.
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        
        
        
        
        
        
        
        