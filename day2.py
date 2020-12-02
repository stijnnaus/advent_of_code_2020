# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:12:16 2020

@author: stijn
"""

def read_password_policy():
    fname = 'input/input_day2.txt'
    with open(fname) as f:
        password_policy = [line.split() for line in f.readlines()]
        
    return password_policy

def count_valid_passwords(password_policy, rules):
    
    num_valid_passwords = 0
    for entry in password_policy:
        valid_password = check_entry(entry, rules)
        num_valid_passwords += valid_password
        
    return num_valid_passwords

def check_entry(entry, rules):
    
    (par_low, par_high), letter, password = parse_entry(entry)
    
    if rules == 'lettercount':
        nletter = password.count(letter)
        valid = (nletter>=par_low and nletter<=par_high)
        
    elif rules == 'letterposition':
        subpassword = password[par_low-1] + password[par_high-1]
        valid = (subpassword.count(letter)==1)  
        
    return valid
    
def parse_entry(entry):
    
    rule_count  = [int(i) for i in entry[0].split('-')]
    rule_letter = entry[1][0]
    password    = entry[2]
    
    return rule_count, rule_letter, password


password_policy = read_password_policy()
rules = 'letterposition'
num_valid_passwords = count_valid_passwords(password_policy, rules=rules)
    
print( f"Number of valid passwords: {num_valid_passwords}")