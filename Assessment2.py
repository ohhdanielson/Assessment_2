# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:03:20 2017

@author: Danielson
"""
#import functions
import csv
import matplotlib
import random

#number of drunks to create
num_of_drunks = 25 

#Number of steps for the drunks
num_of_steps = 500

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



"""
#distance between 2 agents
answer = (((drunks[0][0] - drunks[1][0])**2) + ((drunks[0][1] - drunks[1][1])**2))**0.5
print(answer) """

#print all drunks after a step
print (drunks)

#loop through drunks
for y in range (num_of_drunks):
    print ((drunks[y][1],drunks[y][0]))
    


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
print (environment[150][128:149]) #number 1's on grid - pub point"""


#create a variable for pub
pub = (environment[149][128:149],environment[150][128:149],environment[151][128:149],environment[152][128:149],environment[153][128:149],environment[154][128:149],environment[154][128:149],environment[155][128:149],environment[156][128:149],environment[157][128:149],environment[158][128:149],)
print (pub)


"""
#drunks 250 home
print (environment[32][21:32])
print (environment[23][21:32])"""

#create variable for the house of drunk 250
drunk250House = (environment[23][21:32],environment[24][21:32],environment[25][21:32],environment[26][21:32],environment[27][21:32],environment[28][21:32],environment[29][21:32],environment[30][21:32],environment[31][21:32],environment[32][21:32])
print (drunk250House)

#print drunk 24 (250)
print (drunks[24])

#Give drunk 250 a variable
drunk250 = drunks[24]

print (drunk250)

#move drunk 24 (250) to his house (drunk250house) 
for y in range (num_of_steps):
    if random.random() < 0.5:
        (drunk250) += 1
    else:
        (drunk250) -=1

print (drunk250)



#plot points on a scatter map
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
for y in range (num_of_drunks):
    matplotlib.pyplot.scatter(drunks[y][1],drunks[y][0])
matplotlib.pyplot.show()


#plot drunks at the pub in the environment
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_drunks):
    matplotlib.pyplot.scatter(drunks[y][1],drunks[y][0])
matplotlib.pyplot.show()
    
#a = environment[y][x]

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()"""