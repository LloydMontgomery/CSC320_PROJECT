CSC 320 Project
By: 
Lloyd Montgomery - V00738451
Chris Cook 		 - V00182284
Parker Atkins	 - V00

-------------------------------------------------------------------------------

Global Pre-Conditions:
	- Python 2.7 installed
	- minisat installed

-------------------------------------------------------------------------------
Base Assignment Files - Minimal Encoding using miniSAT - 12/15
-------------------------------------------------------------------------------
How to execute all files for 12/15 marks:

> python generateMinimalEncoding.py
> python sudokuToCNF.py testsudoku.txt minimalEncoding.txt
> minisat testsudoku_minimalEncoding.txt testDud-minEnc-minisat.txt
> python outputFormatter.py <testDud-minEnc-minisat.txt>

-------------------------------------------------------------------------------
File: generateMinimalEncoding.py

To execute:
> python generateMinimalEncoding.py

Ouput:
minimalEncoding.txt

-------------------------------------------------------------------------------
File: sudokuToCNF.py

Pre-Condition:
	- helperLibrary.py is in the same directory
	- <sudoku file> has format: contiguous string of 81 characters on the
	  first line of the .txt file where all digits are sudoku numbers and all 
	  other characters represent blank spaces
	  EX: "000083900100000030004000070042030000600000004000070010020000000080009200000250006"
	- <encoding file> has standard format: simplified "DIMACS CNF" format

To Execute (General Format):
> python sudokuToCNF.py <sudoku file> <encoding file>

To Execute (with files given):
> python sudokuToCNF.py testsudoku.txt minimalEncoding.txt

Ouput:
<sudoku file name>_<encoding file name>.txt

-------------------------------------------------------------------------------
File: outputFormatter.py

Pre-Conditions:
	- helperLibrary.py is in the same directory

To Execute (General Format):
> python outputFormatter.py <SAT solver output file>

To Execute (with files given):
> python outputFormatter.py <*******************>

Output:
Prints the output of the SATsovler back into a solved sudoku puzzle (prettyprinting)
EX:
--- Soduku Solution ---
 4 1 7 | 3 6 9 | 8 2 5
 6 3 2 | 1 5 8 | 9 4 7
 9 5 8 | 7 2 4 | 3 1 6
-------+-------+-------
 8 2 5 | 4 3 7 | 1 6 9
 7 9 1 | 5 8 6 | 4 3 2
 3 4 6 | 9 1 2 | 7 5 8
-------+-------+-------
 2 8 9 | 6 4 3 | 5 7 1
 5 7 3 | 2 9 1 | 6 8 4
 1 6 4 | 8 7 5 | 2 9 3










EVERYTHING BELOW HERE IS NOT COMPLETE, PIECES OF THE FINAL README

- ADD STUFF FOR NORVIG (inc. times, etc.)
- ADD STUFF FOR SATZ (inc. times, sizes, etc.)
- ADD STUFF FOR EXTENDED & EXTENDED2 ENCODING

-------------------------------------------------------------------------------
File: generateExtendedEncoding.py

To execute:
python generateExtendedEncoding.py

Ouput:
extendedEncoding.txt
-------------------------------------------------------------------------------
File: generateExtendedEncoding2.py

To execute:
python generateExtendedEncoding2.py

Ouput:
extendedEncoding2.txt
-------------------------------------------------------------------------------
File: generateExtendedEncoding2.py

To execute:
python generateExtendedEncoding2.py

Ouput:
extendedEncoding2.txt
-------------------------------------------------------------------------------
