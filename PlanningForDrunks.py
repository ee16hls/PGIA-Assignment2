#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:05:06 2019
Programming for Geographical Information Analysis: Core Skills 2018
Model run script- Assignment 2- Planning for Drunks
@author: hannahsherwood

This code when run, starts an agent based model which is created here to model the movement of drunk agents passing through 
their environment from the pub to their homes. The code reads in a text file which provides the environment information and 
includes locations of pubs and agent homes. The drunk agent framework is also read into the code and this sets the 
behaviours of the drunk agents. The models code calculates where the pubs and homes are located and assigns each drunk agent
a starting location in the pub and an ending location in their homes.

Once home, the code will produce two windows, one showing the final environment map with the drunk agents all back in their 
homes after their journey. The second window is a density map showing the amount of times each cell on the map has been 
walked over by the drunk agents tryig to find their way home. An output file is also created and saved as a csv file format 
containing the walked in environment density data. 

"""

"""
Imports
""" 
import tkinter
import matplotlib
import matplotlib.pyplot
matplotlib.use('TkAgg')
matplotlib.use('macosx')
import matplotlib.animation
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
            x_startpoint = x
            y_startpoint = y
            

"""
Gives each agent a housenumber and assigns agents with a starting location at one of the pubs in the area. 
"""
for j in range(num_of_agents):
    housenumber = (j+1)*10
    agents.append(Drunk_AgentFramework.Agent(environment, agents, housenumber, x_startpoint, y_startpoint))
    


"""
Gets agents to move through the environment and get home. The 'if' function is for agents that make it home
as they fulfill the TRUE statement and the code can stop running as their location is the same as their assigned housenumber.
"""

for i in range (num_of_agents):
    while agents[i].got_home==False:
        agents[i].move()
        walked_through_env[agents[i]._y][agents[i]._x]+=1
        if agents[i].environment[agents[i]._y][agents[i]._x]==agents[i].housenumber: 
            agents[i].got_home=True
           

"""
Creates the figure showing drunk agents in their homes after their journey from the pub.
"""
	
fig.canvas.set_window_title('Drunk agents having arrived back home')
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()


"""
Writes the stored values from the walked_through_environment list to a csv file to build the density map
"""

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


"""
Defines the gen_function for the animation
"""

def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 100) & (carry_on) :
        yield a 
        a = a + 1 


"""
Creates the GUI window for the model to run in

"""
root = tkinter.Tk()
root.wm_title("Model")
 

"""
Defines the 'run' function in the model to begin animation 
"""   

def run():
    global animation 
    animation = matplotlib.animation.FuncAnimation(fig, frames=gen_function, repeat=False)
    canvas.show()

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



"""
Adds a menu bar and 'run' button for users to start the model run
"""

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() #Waits for interactions.
