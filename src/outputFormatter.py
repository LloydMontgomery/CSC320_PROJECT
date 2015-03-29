#!/usr/bin/python
import sys
import helperLibrary

miniSATOutputFile = 0

def initFileHandles():
    global miniSATOutputFile

    if len(sys.argv) == 1:
        print "Missing a command-line argument: filename of MiniSAT output"
        return
    
    miniSATOutputFile = open(sys.argv[1], "r")
    
def closeFileHandles():
    global miniSATOutputFile
    
    miniSATOutputFile.close()

# Check if sodoku puzzle was satisfiable 
def checkSatisfiability():
    global miniSATOutputFile
    
    solvable = miniSATOutputFile.readline()
    print solvable
    if(solvable == "UNSAT\n"):
        print "CNF was unsatisfiable"
        return
    
    if(solvable == "SAT\n"):
        formatter()

def formatter(): 
    global miniSATOutputFile
    
    #sudoku = [[None]*9]*9
    sudoku = [[None],[None],[None],[None],[None],[None],[None],[None],None],
             [[None],[None],[None],[None],[None],[None],[None],[None],[None]],
             [[None],[None],[None],[None],[None],[None],[None],[None],[None]],
             [[None],[None],[None],[None],[None],[None],[None],[None],[None]],
             [[None],[None],[None],[None],[None],[None],[None],[None],[None]],
             [[None],[None],[None],[None],[None],[None],[None],[None],[None]],
             [[None],[None],[None],[None],[None],[None],[None],[None],[None]],
             [[None],[None],[None],[None],[None],[None],[None],[None],[None]],
             [[None],[None],[None],[None],[None],[None],[None],[None],[None]],
    CFN = miniSATOutputFile.readline()

    for s in CFN.split():
        # Filter out negative digits 
        if s.isdigit():
            if int(s) != 0:
                variables = helperLibrary.base9Toxyz(int(s))
                sudoku[variables[1]-1][variables[0]-1] = variables[2]                             
               
    print sudoku

  
def main():
    initFileHandles()
    checkSatisfiability()
    closeFileHandles()

main()

