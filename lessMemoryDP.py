class DynamicProgramming(object):
	def __init__(self, capacity , values , weights):
		"""
			capacity : int,capacity of bag
			values, weights : list
		"""
		self.capacity = capacity
		self.values = values
		self.weights = weights
		self.numItems = len(values)
		#self.iteration = 0
		
	def newList(self):
		"""
			k : int denotes length of list, all initialized to 0
		"""
		tempList = []
		i = 0
		while i <= self.capacity:
			tempList.append(0)
			i += 1
		return tempList
		
	def dynamicProgramming(self):
		#print "Hi"
		col1 = self.newList()
		col2 = self.newList()
		#col2[0][1].append(5)
		#col2[1][1].append(5)
		#col2[0][1].append(5)
		#print col1
		#print col2
		k,j = 0,0
		#col2[k][1].append(0)
		for j in xrange(1,self.numItems + 1):		#[1,numItems]
			for k in xrange(0,self.capacity + 1):	#k : capacity [1,capacity]
				if self.weights[j - 1] > k:
					
					col2[k] = col1[k]	#0 denotes dat jth iitem is not taken 2 optimally fill d bag of wt w frm items [1,j]
				else:
					
					col2[k] = max(col1[k] , self.values[j - 1] + col1[k  - self.weights[j - 1]])
			#print col2	
			col1 = col2
			col2 = self.newList()
			print k,j
		return col1[self.capacity]

def solveIt(inputData):
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
		
	#print values
	#print weights
	dp = DynamicProgramming(capacity , values , weights)
	maxPossible = dp.dynamicProgramming()
	return maxPossible

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
        
