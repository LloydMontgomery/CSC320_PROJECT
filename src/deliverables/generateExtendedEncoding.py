# Authors: Lloyd, Chris, Parker
# March 29th, 2015
# 
# Generates an extended encoding in CNF and outputs to a file called: "extendedEncoding.txt"

#!/usr/bin/python
import helperLibrary

def buildClauses():
    file = open('extendedEncoding.txt', 'w+')
    file.write('c The extended encoding\n')
    file.write('p cnf 729 11745\n')
 
    # At least one number in each entry:
    for y in range(1, 10):
        for x in range(1, 10):
            for z in range(1, 10):
                file.write(str(helperLibrary.xyzToBase9(x, y, z)) + " ")    
            file.write("0\n")
          
    # Each number appears at most once in each row:
    for y in range(1, 10):
        for z in range(1, 10):
            for x in range(1, 10):
                for i in range ((x+1), 10):
                    file.write("-" + str(helperLibrary.xyzToBase9(x, y, z)) + " -" + str(helperLibrary.xyzToBase9(i, y, z)) + " 0\n")    

 
    # Each number appears at most once in each column:
    for x in range(1, 10):
        for z in range(1, 10):
            for y in range(1, 10):
                for i in range ((y+1), 10):
                    file.write("-" + str(helperLibrary.xyzToBase9(x, y, z)) + " -" + str(helperLibrary.xyzToBase9(x, i, z)) + " 0\n")    
 
    # Each number appeats at most once in each 3x3 sub-grid:
    for z in range(1, 10):
        for i in range(0, 3):
            for j in range(0, 3):
                for x in range(1, 4):
                    for y in range(1, 4):
                        for k in range((y+1), 4):
                            file.write("-" + str(helperLibrary.xyzToBase9((3*i+x), (3*j+y), z)) + " -" + str(helperLibrary.xyzToBase9((3*i+x),(3*j+k), z)) + " 0\n")    
    for z in range(1, 10):
        for i in range(0, 3):
            for j in range(0, 3):
                for x in range(1, 4):
                    for y in range(1, 4):
                        for k in range((x+1), 4):
                            for l in range(1, 4):
                                file.write("-" + str(helperLibrary.xyzToBase9((3*i+x), (3*j+y), z)) + " -" + str(helperLibrary.xyzToBase9((3*i+k),(3*j+l), z)) + " 0\n")    
    
    # Each number appears at most once in each entry:
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                for i in range ((z+1), 10):
                    file.write("-" + str(helperLibrary.xyzToBase9(x, y, z)) + " -" + str(helperLibrary.xyzToBase9(x, y, i)) + " 0\n")    

    file.close()

buildClauses()   
