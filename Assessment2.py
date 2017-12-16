# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:13:06 2017

@author: hardwickd
"""
import csv

f = open('drunk.txt', newline='')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

"""for row in dataset: #a list of all values in each row
    print (row) #print all rows in the .csv file"""
    
for row in dataset: # create a list for each row in csv file
    rowlist = []
    for value in row: # populate/append the list with the value of each row
        rowlist.append(value)
        print (rowlist)
    
