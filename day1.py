# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:19:03 2020

@author: stijn
"""

fname = 'input/input_day1.txt'
with open(fname) as f:
    report = [int(line) for line in f.readlines()]
  
    
# Part 1: Two numbers that sum to 2020
for number1 in report:
    number2 = 2020-number1 # The number we need to get 2020
    if number2 in report:
        output = number1*number2
        break

print (f"PART 1| Output = {output}")

# Part 2: Three numbers that sum to 2020
for number1 in report:
    for number2 in report:
        number3 = 2020 - number1 - number2
        
        if number3 in report:
            output = number1*number2*number3
            break
            

print (f"PART 2| Output = {output}")