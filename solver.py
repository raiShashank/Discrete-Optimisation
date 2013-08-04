#!/usr/bin/python
# -*- coding: utf-8 -*-


def solveIt(inputData):
	# Modify this code to run your optimization algorithm
	
	# parse the input
	lines = inputData.split('\n')
	
	firstLine = lines[0].split()
	items = int(firstLine[0])
	capacity = int(firstLine[1])
	
	values = []
	weights = []
	
	for i in range(1, items+1):
		line = lines[i]
	
		parts = line.split()
		
		values.append(int(parts[0]))
		weights.append(int(parts[1]))
	#print weights[0]
	#print weights[1]
	#print weights[2]
	#rint weights[3]
	
	#outputData = len(values)
	#print values
	#print weights
	# a trivial greedy algorithm for filling the knapsack
	# it takes items in-order until the knapsack is full
	O = []
	#row = []
	for i in xrange(capacity + 1):
		O.append([])
		for j in xrange(items + 1):
			O[i].append(0)
		
	#for i in xrange(1,items + 1):
	#	O[0].append(0)
	#O[0][0] = 5
	#print O
	#print O[0][3]
	for j in xrange(1,items + 1):
		for k in xrange(1,capacity + 1):
			#print k,j
			if weights[j - 1] > k:
				O[k][j] = O[k][j - 1]
			else:
				O[k][j] = max(values[j - 1] + O[k - weights[j - 1]][j - 1], O[k][j - 1])
				
	#for i in xrange(capacity + 1):
	#	print O[i]
			
	value = O[capacity][items]
	taken = []
	k = capacity
	j = items
	while j > 0 :
		if O[k][j] == O[k][j - 1]:
			taken = [0] + taken
		else:
			taken = [1] + taken
			k = k - weights[j - 1]
		j -= 1
	#print taken
	#for i in range(0, items):
	#if weight + weights[i] <= capacity:
	    #taken.append(1)
	    #value += values[i]
	    #weight += weights[i]
	#else:
	    #taken.append(0)
	
	## prepare the solution in the specified output format
	outputData = str(value) + ' ' + str(1) + '\n'
	outputData += ' '.join(map(str, taken))
	return outputData
	

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

