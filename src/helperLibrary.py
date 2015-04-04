# Authors: Lloyd, Chris, Parker
# March 29th, 2015
# 
# Contains functions that are used by other Python scripts in this folder

# def xyzToBase9(x, y, z):
#
# Parameters: x - Column
#			  y - Row
#			  z - Entry
#
# Returns: The base 9 as if xyz was a base 10 number
#
def xyzToBase9(x, y, z):
	# 81*(y - 1) + 9*(x - 1) + (z - 1) + 1
	return (81*(y - 1) + 9*(x - 1) + z)

# def base9Toxyz(n):
#
# Parameters: n - Base 9 number to be decomposed
#
# Returns: The decomposed number
#
def base9Toxyz(n):
	n = n - 1
	x = ((n % 81) / 9) + 1
	y = (n / 81) + 1
	z = (n % 9) + 1
	return [x, y, z]