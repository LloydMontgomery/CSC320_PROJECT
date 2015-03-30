#!/usr/bin/python
import sys
import helperLibrary

miniSATOutputFile = 0

def initFileHandles():
    global miniSATOutputFile

    if len(sys.argv) == 1:
        print "Missing a command-line argument: filename of MiniSAT output"
        return 0
    
    miniSATOutputFile = open(sys.argv[1], "r")
    return 1
    
def closeFileHandles():
    global miniSATOutputFile
    
    miniSATOutputFile.close()

# Check if sodoku puzzle was satisfiable 
def checkSatisfiability():
    global miniSATOutputFile
    
    # solvable = miniSATOutputFile.readline()
    # print solvable

    # if(solvable == "SAT\n"):
    #     formatter()
    # else:
    #     print "CNF was unsatisfiable"

def formatter(): 
    global miniSATOutputFile
    
    #sudoku = [[]*9]*9
    sudoku = [[0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]
    CFN = miniSATOutputFile.readline()

    for s in CFN.split():
        # Filter out negative digits 
        if s.isdigit():
            if int(s) != 0:
                variables = helperLibrary.base9Toxyz(int(s))
                sudoku[variables[1]-1][variables[0]-1] = variables[2]                             
               
    print sudoku

  
def main():
    if not initFileHandles():
        return
    # checkSatisfiability()
    formatter()
    closeFileHandles()

main()

