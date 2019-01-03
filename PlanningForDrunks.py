#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:05:06 2019

@author: hannahsherwood
"""

"""
Imports
""" 
import matplotlib
import matplotlib.pyplot
matplotlib.use('TkAgg')
matplotlib.use('macosx')
import csv
import Drunk_AgentFramework


"""
Create lists 
"""
environment = []
agents = []
walked_through_env = []


"""
Define agent parameters 
"""
num_of_agents = 25


"""
Defines the environment frame size in the figure
"""
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


"""
Reads in the environmnet text file 
"""
f = open ("TownPlan.txt")
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)


"""
Changes the environment data from CSV format into rows
"""
for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
   
    environment.append(rowlist)
    
    
"""
Creates the output for the density map showing the number of drunks 
passing through each point on the map. 
"""

for i in range(300):
    rowlist = []
    for j in range(300):
        rowlist.append(0)
    walked_through_env.append(rowlist)
    


"""
Locates the pubs within the environment data and assigns them a value of 1. 
"""

for y, row in enumerate(environment):
    for x, value in enumerate (row):
        if value == 1:
            xstartpoint = x
            ystartpoint = y
            

"""
Gives each agent a housenumber and assigns agents with a starting location at one of the pubs in the area. 
"""
for j in range(num_of_agents):
    housenumber = (j+1)*10
    agents.append(Drunk_AgentFramework.Agent(environment, agents, housenumber, xstartpoint, ystartpoint))
    


# For agents that aren't home, continue moving and store 1 into the stepped_environment file


for i in range (num_of_agents):
    while agents[i].got_home==False:
        agents[i].nav()
        walked_through_env[agents[i]._y][agents[i]._x]+=1
        # For agents that made it home, set their arrival status to True to stop the code from rerunning those agents, and tell them to drunkely announce their arrival
        if agents[i].environment[agents[i]._y][agents[i]._x]==agents[i].housenumber: # If the agent's location is the same as their house number
            agents[i].got_home=True
           


# Create a graph to demonstrate the agents that arrived at their house (all of them by this point due to above code)
	
fig.canvas.set_window_title('Drunk agents having arrived back home')
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()




# Write stored values from the stepped_environment list to be able to create a density map


f2= open ('walked_enviroment_output.csv', 'w', newline= '')
writer = csv.writer (f2, delimiter = ',')
for row in walked_through_env:
    writer.writerow(row)
f2.close


"""
Creates a new list for the denisty values of the walked through environment
"""
walked_environment_output = []


"""
Reads in the walked_environment_output file
"""

f=open ("walked_enviroment_output.csv")
reader=csv. reader (f, quoting = csv.QUOTE_NONNUMERIC)


"""
Changes data format from CSV to rows 
"""

for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    walked_environment_output.append(rowlist)



"""
Defines the size of the density map
"""

fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])


"""
Displays the density map showing the density of drunks passing through each 
point on the map. 
"""

fig.canvas.set_window_title('Density Map')
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(walked_environment_output)
matplotlib.pyplot.show()

