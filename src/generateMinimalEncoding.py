#!/usr/bin/python

def buildClauses():
    file = open('minimalEncoding.txt', 'w+')
    file.write('c The minimal encoding\n')
    file.write('p cnf 730 8829\n')
    file.close()
    
    # At least one number in each entry:

    # Each number appears at most once in each row:

    # Each number appears at most once in each column:

    # Each number appeats at most once in each 3x3 sub-grid:
 
buildClauses()   
