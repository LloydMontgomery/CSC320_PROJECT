#!/usr/bin/python
import sys
import helperLibrary

sudokuFile = 0
sodukuLookupTable = [0]*729

def initFileHandles():
	global sudokuFile
	if len(sys.argv) == 1:
		print "Missing a command-line argument: filename of input sudoku problem"
		return
	sudokuFile = open(sys.argv[1], "r")

def closeFileHandles():
	global sudokuFile
	sudokuFile.close()

def convertSudoku():
	global sudokuFile
	sudoku = sudokuFile.readline()
	if len(sudoku) != 81:
		print "Sudoku file is of incorrect format"

	x = y = 1
	for i in range(0, 81):
		if sudoku[i].isdigit() and int(sudoku[i]) > 0:
			index = helperLibrary.xyzToBase9(x, y, int(sudoku[i]))
			sodukuLookupTable[index] = 1
		x += 1
		if x == 10:
			x = 1
			y += 1


	print sodukuLookupTable[4]



def main():
	initFileHandles()
	convertSudoku()


	closeFileHandles()
	
main()
