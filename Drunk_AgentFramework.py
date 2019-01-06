#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:06:32 2019
Programming for Geographical Information Analysis: Core Skills 2018
Model Agent Framework- Assignment 2- Planning for Drunks
@author: hannahsherwood
"""
"""
This code creates the agents Class to be used in the agent-based model.
Here the agents have their 'behaviours' defined for them to interact within a
set environment. The 'drunk' agents are assigned a starting location at a 'pub' 
and a housenumber which corresponds to a location number on the towns map. The 
agents are set to move randomly from the pub (start location) until they reach 
home.

"""

"""
Imports
"""
import random


"""
Create the Agent class and define their characteristics. Agents are placed in 
their environment, made to be self-aware and aware of each other, assigned a
housenumber, agent is set in a starting x and y location of a pub, and agents 
are told not to start the model run at their homes. 
"""
class Agent ():
    
    def __init__(self, environment, agents, housenumber, x_startpoint, y_startpoint):
        
        self.environment = environment
        self.agents = agents
        self.housenumber = housenumber
        self._x = x_startpoint
        self._y = y_startpoint
        self.got_home = False

   
    """
    Defines the move function. This function allows the drunk agents to move around 
    the environment randomly but they are set a limit where the boundaries of the
    environment exist. 
    """
        
    def move (self):
        
        if random.random() <0.5:
            xmove=self._x+1
            if xmove<len(self.environment) and xmove>0:
                self._x = xmove
              
        else:
            xmove=self._x-1
            if xmove<len(self.environment) and xmove>0:
                self._x = xmove
                        
                
        if random.random() <0.5:
            ymove=self._y+1
            if ymove<len(self.environment) and ymove>0:
                self._y = ymove
                
        else:
            ymove=self._y-1
            if ymove<len(self.environment) and ymove>0:
                self._y = ymove
                