#!/usr/bin/python
import sys
import helperLibrary

sudokuFile = 0
minimalEncodingFile = 0
sudokuMinEncodingFile = 0
sudokuNumbers = []
#sodukuLookupTable = [[None]*9]*9

def initFileHandles():
	global sudokuFile, minimalEncodingFile, sudokuMinEncodingFile

	if len(sys.argv) == 1:
		print "Missing a command-line argument: filename of input sudoku problem"
		return
	sudokuFile = open(sys.argv[1], "r")

	minimalEncodingFile = open("minimalEncoding.txt", "r+")
	sudokuMinEncodingFile = open(sudokuFile.name[:-4] + "_minimalEncoding.txt", "w+")

def closeFileHandles():
	global sudokuFile, minimalEncodingFile, sudokuMinEncodingFile

	sudokuFile.close()
	minimalEncodingFile.close()
	sudokuMinEncodingFile.close()

def convertSudoku():
	global sudokuFile, sudokuNumbers

	sudoku = sudokuFile.readline()
	if len(sudoku) != 81:
		print "Sudoku file is of incorrect format"

	x = y = 1
	for i in range(0, 81):
		if sudoku[i].isdigit() and int(sudoku[i]) > 0:
			sudokuNumbers.append(helperLibrary.xyzToBase9(x, y, int(sudoku[i])))
		x += 1
		if x == 10:
			x = 1
			y += 1
	#print sudokuNumbers
	
	# converts the given sudoku into a lookup-table for constant-time checking
	# x = y = 1
	# for i in range(0, 81):
	# 	if sudoku[i].isdigit() and int(sudoku[i]) > 0:
	# 		index = helperLibrary.xyzToBase9(x, y, int(sudoku[i]))
	# 		sodukuLookupTable[index] = 1
	# 	x += 1
	# 	if x == 10:
	# 		x = 1
	# 		y += 1

def addSudokuToMinimalEncodingFile():
	global sudokuNumbers, minimalEncodingFile, sudokuMinEncodingFile

	# Read the first two lines, skip the first
	minimalEncodingBuffer = minimalEncodingFile.readline()
	sudokuMinEncodingFile.write(minimalEncodingBuffer)
	minimalEncodingBuffer = minimalEncodingFile.readline()

	# Split the input into 4 pieces so we can add to the number of clauses
	minimalEncodingBuffer = minimalEncodingBuffer.split()
	clauses = int(minimalEncodingBuffer[3])
	clauses += len(sudokuNumbers)
	
	# Cast the number of clauses back into a str and write to file
	minimalEncodingBuffer[3] = str(clauses)
	minimalEncodingBuffer = " ".join(minimalEncodingBuffer)
	sudokuMinEncodingFile.write(minimalEncodingBuffer + "\n")

	# Copy all the existing clauses as is
	while True:
		minimalEncodingBuffer = minimalEncodingFile.readline()
		if minimalEncodingBuffer == "":
			break
		sudokuMinEncodingFile.write(minimalEncodingBuffer)

	# Write the sudoku truth clauses as clauses in the minimal encoding
	for number in sudokuNumbers:
		sudokuMinEncodingFile.write(str(number) + " 0\n")


def main():
	initFileHandles()
	convertSudoku()
	addSudokuToMinimalEncodingFile()
	closeFileHandles()
	
main()
