#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:06:32 2019

@author: hannahsherwood
"""

"""
Imports
"""
import random


"""
Create the Agent class and define their characteristics
"""
class Agent ():
    
    def __init__(self, environment, agents, housenumber, x_startpoint, y_startpoint):
        
        """
        Constructing the Agent class; assigning class variables
        1. Place agents in the environment
        2. Make agents self-aware and of others
        3. Assign each agent a house number
        4. Set agent starting x coordinate to start the at the pub location
        5. Set agent starting y coordinate to start the at the pub location
        6. Add variable to set agent not at home at the start of the model        
        """
        
        self.environment = environment
        self.agents = agents
        self.housenumber = housenumber
        self._x = x_startpoint
        self._y = y_startpoint
        self.got_home = False
        
        
        
    def move (self):
        
        """
        Defining the nav function; allowing drunk agents to navigate the environment
        1. They are limited to walk between the environment edges; thus no torus is implemented
        2. Each agent takes a step in a random direction
        """
        
        if random.random() <0.5:
            xmove=self._x+1
            if xmove<len(self.environment) and xmove>0:
                self._x = xmove
                #self.numofsteps +=1
        else:
            xmove=self._x-1
            if xmove<len(self.environment) and xmove>0:
                self._x = xmove
                #self.numofsteps +=1            
                
        if random.random() <0.5:
            ymove=self._y+1
            if ymove<len(self.environment) and ymove>0:
                self._y = ymove
                #self.numofsteps +=1
        else:
            ymove=self._y-1
            if ymove<len(self.environment) and ymove>0:
                self._y = ymove
                #self.numofsteps +=1