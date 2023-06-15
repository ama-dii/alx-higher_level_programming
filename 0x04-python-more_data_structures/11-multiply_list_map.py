#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
	"""
	function that returns a list with all values multiplied by a number
	without using any loops
	...
	parameters
	----------
	my_list - a list

	Return - 
	a new list
	Same length as my_list
	Each value should be multiplied by number
	"""

    return (list(map(lambda x: x * number, my_list)))

