# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:03:20 2017

@author: Danielson
"""
#import functions
import csv
import matplotlib
import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import math

#number of drunks to create
num_of_drunks = 25 
infinity_moves = math.inf

#Number of steps for the drunks
num_of_steps = 1000

#open drunk.txt
f = open('drunk.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#Make an empty environment list and append values of rowlist into it, making 2D datatset
environment = [] 
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)

#loop thorugh environment rows to identify row values for homes and pub
for num, name in enumerate(environment, start=1):
    print("environment {}: {}".format(num, name))
           
"""
print (environment[150]) #row containing 1's 
print (environment[150][128:149]) #number 1's on grid - pub point
"""

#create a variable for pub
pub = (environment[149][128:149],environment[150][128:149],environment[151][128:149],environment[152][128:149],environment[153][128:149],environment[154][128:149],environment[154][128:149],environment[155][128:149],environment[156][128:149],environment[157][128:149],environment[158][128:149],)
print (pub)

#Create a blank list for drunks
drunks = []

#Create 25 drunks using a loop
for i in range (num_of_drunks):
    drunks.append([150,145])
    
print (drunks)

#make each drunk walk a random step
for y in range (num_of_drunks):
    if random.random() < 0.5:
        (drunks[y][0]) += 1
    else:
        (drunks[y][0]) -=1
    if random.random() < 0.5:
        (drunks[y][1]) += 1
    else:
        (drunks[y][1]) -=1

#print all drunks after a step
print (drunks)  

"""
#plot drunks on a scatter map
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
for y in range (num_of_drunks):
    matplotlib.pyplot.scatter(drunks[y][1],drunks[y][0])
matplotlib.pyplot.show()
"""


"""
#loop through drunks
for y in range (num_of_drunks):
    print ((drunks[y][1],drunks[y][0]))
"""

"""
#Loop through list using nested loop
for i in range (len(environment)):
    for j in range (len(environment)):
        print(environment[i][j])
        if (drunks[24] ==(drunk250house)):
            print = ("Honey I'm home")
"""


#move drunk 24 (250) 1000 times
for y in range (num_of_steps):
    if random.random() < 0.5:
        (drunks[24][0]) += 1
    else:
        (drunks[24][0]) -= 1
    if random.random() < 0.5:
        (drunks[24][1]) +=1 
    else:
        (drunks[24][1]) -= 1


"""
#Torus method for drunks      
for y in range (num_of_steps):
    if random.random() < 0.5:
        drunks[24][0] = (drunks[24][0] + 1) %100
    else:
        drunks[24][0] = (drunks[24][0] - 1) %100
    if random.random() < 0.5:
        drunks[24][1] = (drunks[24][1] + 1) %100
    else:
        drunks[24][1] = (drunks[24][1] - 1) %100
    if (drunks[24] == drunk250house):
        print ("home")
        break
    else:
        print ("still lost")
"""

#create variable for the house of drunk 250
drunk250house = (environment[23][21:32],environment[24][21:32],environment[25][21:32],environment[26][21:32],environment[27][21:32],environment[28][21:32],environment[29][21:32],environment[30][21:32],environment[31][21:32],environment[32][21:32])
print (drunk250house)

#Give drunk 24(house 250) a variable
drunk250 = drunks[24]

print (drunk250)

"""
for y in range (num_of_steps):
    if random.random() < 0.5:
        (drunks[24][0]) += 1
    else:
        (drunks[24][0]) -= 1
    if random.random() < 0.5:
        (drunks[24][1]) +=1 
    else:
        (drunks[24][1]) -= 1
    if (drunks[24] == drunk250house):
        print ("home")
        break
    else:
        print ("still lost")
"""

#plot drunks at the pub in the area file (environment)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_drunks):
    matplotlib.pyplot.scatter(drunks[i][1],drunks[i][0])
matplotlib.pyplot.show()

"""
#move drunk 24 (250) until he reaches drunk250house
for drunks in range:
    if drunks[24] == drunk250house:
        break
    print ('Reached home')
"""

"""
#distance between 2 agents
answer = (((drunks[0][0] - drunks[1][0])**2) + ((drunks[0][1] - drunks[1][1])**2))**0.5
print(answer) 
"""

