# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:19:21 2020

@author: stijn
"""

def readTreeMap():
    fname = "input/input_day3.txt"
    with open(fname,'r') as f:
        treeMap = f.read().split()
    return treeMap        

def countTreesInDescent(treeMap, stepSize):
    
    stepRight, stepDown = stepSize
    numRow = len(treeMap)
    numCol = len(treeMap[0])
    iDown = 0
    iRight = 0
    numTrees = 0
    while iDown<numRow:
        iRight = iRight%numCol
        if treeMap[iDown][iRight]=='#':
            numTrees += 1
       
        iRight += stepRight
        iDown  += stepDown
        
    return numTrees
    

stepSize = [3,1]
treeMap = readTreeMap()
numTrees = countTreesInDescent(treeMap, stepSize)
    
print( f"PART 1 | Total number of trees: {numTrees}" )
    
stepSizeAll = [[1,1], [3,1], [5,1], [7,1], [1,2]]
numTreesProduct = 1
for stepSize in stepSizeAll:
    
    numTrees = countTreesInDescent(treeMap, stepSize)
    numTreesProduct *= numTrees
    
print( f"PART 2 | Product of tree numbers: {numTreesProduct}" )








