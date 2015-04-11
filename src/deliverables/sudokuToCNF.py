#!/usr/bin/python
import sys
import helperLibrary

sudokuFile = 0
encodingFile = 0
sudokuEncodingFile = 0
sudokuNumbers = []

def initFileHandles():
	global sudokuFile, encodingFile, sudokuEncodingFile

	if len(sys.argv) < 3:
		print "Missing a command-line argument: <sudoku puzzle> <CNF encoding>"
		return

	sudokuFile = open(sys.argv[1], "r")

	encodingFile = open(sys.argv[2], "r+")
	sudokuEncodingFile = open(sudokuFile.name[:-4] + "_" + encodingFile.name, "w+")

def closeFileHandles():
	global sudokuFile, encodingFile, sudokuEncodingFile

	sudokuFile.close()
	encodingFile.close()
	sudokuEncodingFile.close()

def convertSudoku():
	global sudokuFile, sudokuNumbers

	sudoku = sudokuFile.readline()
	if len(sudoku) < 81:
		print len(sudoku)
		print "Sudoku file is of incorrect format"

	x = y = 1
	for i in range(0, 81):
		if sudoku[i].isdigit() and int(sudoku[i]) > 0:
			sudokuNumbers.append(helperLibrary.xyzToBase9(x, y, int(sudoku[i])))
		x += 1
		if x == 10:
			x = 1
			y += 1

def addSudokuToMinimalEncodingFile():
	global sudokuNumbers, encodingFile, sudokuEncodingFile

	# Read the first two lines, skip the first
	minimalEncodingBuffer = encodingFile.readline()
	sudokuEncodingFile.write(minimalEncodingBuffer)
	minimalEncodingBuffer = encodingFile.readline()

	# Split the input into 4 pieces so we can add to the number of clauses
	minimalEncodingBuffer = minimalEncodingBuffer.split()
	clauses = int(minimalEncodingBuffer[3])
	clauses += len(sudokuNumbers)
	
	# Cast the number of clauses back into a str and write to file
	minimalEncodingBuffer[3] = str(clauses)
	minimalEncodingBuffer = " ".join(minimalEncodingBuffer)
	sudokuEncodingFile.write(minimalEncodingBuffer + "\n")

	# Copy all the existing clauses as is
	while True:
		minimalEncodingBuffer = encodingFile.readline()
		if minimalEncodingBuffer == "":
			break
		sudokuEncodingFile.write(minimalEncodingBuffer)

	# Write the sudoku truth clauses as clauses in the minimal encoding
	for number in sudokuNumbers:
		sudokuEncodingFile.write(str(number) + " 0\n")


def main():
	initFileHandles()
	convertSudoku()
	addSudokuToMinimalEncodingFile()
	closeFileHandles()
	
main()
