import sys
class Table:
	def __init__(self,numItems,numSubsets, matrix):
		"""
			numItems : represents no. of columns in d table
			numSubsets : represents no. of rows in d table
			matrix : d actual table, any object of dis class will have an IV dat points 2 d table
		"""
		self.numItems = numItems
		self.numSubsets = numSubsets
		self.matrix = matrix
		self.itemToSets = {}
		self.setToItems = {}
		self.answer = []
		self.totalItems = range(numItems)
		for i in xrange(numItems):
			self.itemToSets[i] = []
			for j in xrange(numSubsets):
				if self.matrix[j][i] == '1':
					self.itemToSets[i].append(j)
					
		for i in xrange(numSubsets):
			self.setToItems[i] = []
			for j in xrange(numItems):
				if self.matrix[i][j] == '1':
					self.setToItems[i].append(j)
	def __str__(self):
		print self.itemToSets
		print self.setToItems
		answer = ''
		for i in xrange(self.numSubsets):
			answer += str(self.matrix[i] )
			answer += "\n"
		return answer
	
	def greedyAlgo1(self):
		#pass
		remainingItem = {}
		for i in xrange(self.numItems):
			remainingItem[i] = 1
		for i in xrange(self.numSubsets):
			self.answer.append(i + 1)
			items = self.setToItems[i]
			for item in items:
				if remainingItem[item] > 0:
					remainingItem[item] -= 1
				
			s = sum(remainingItem.values())
			if s == 0:
				break
			
	def greedyAlgo2(self):
		remainingItem = {}
		for i in xrange(self.numItems):
			remainingItem[i] = 1
		numOfItems = {}
		for i in xrange(self.numSubsets):
			numOfItems[len(self.setToItems[i])] = numOfItems.get(len(self.setToItems[i]),[])
			numOfItems[len(self.setToItems[i])].append(i)
			
		c = sorted(numOfItems.keys(),reverse = True)
		k = 0
		for i in xrange(self.numSubsets):
			setNo = numOfItems[c[k]].pop()
			self.answer.append(setNo + 1)
			
			if len(numOfItems[c[k]]) == 0:
				numOfItems.pop(c[k])
				k += 1
			items = self.setToItems[setNo]
			for item in items:
				if remainingItem[item] > 0:
					remainingItem[item] -= 1
			
			s = sum(remainingItem.values())
			if s == 0:
				break
				
	def greedyAlgo3(self):
		dynamicSetLength = []
		for i in self.setToItems.keys():
			dynamicSetLength.append(len(self.setToItems[i]))
		remainingItem = {}
		for i in xrange(self.numItems):
			remainingItem[i] = 1
		
		for i in xrange(self.numSubsets):
			setNo = self.findSetWithMaxElements(dynamicSetLength)
			self.answer.append(setNo + 1)
			items = self.setToItems[setNo]
			for item in items:
				if remainingItem[item] > 0:
					remainingItem[item] -= 1
				for sets in self.itemToSets[item]:
					dynamicSetLength[sets] -= 1
					
			
			s = sum(remainingItem.values())
			if s == 0:
				break
				
	def findSetWithMaxElements(self,dynamicSetLength):
		maxIndex = 0
		maxLength = dynamicSetLength[maxIndex]
		for i in xrange(1,self.numSubsets):
			if dynamicSetLength[i] > maxLength:
				maxIndex = i
				maxLength = dynamicSetLength[i]
		return maxIndex
		
def main(inputData):
	"""
		inputData : string read from file which has "\n" for every newline in original file
	"""
	lines = inputData.split('\n')
	firstLine = lines[0].strip().split()
	numItems = int(firstLine[0])
	numSubsets = int(firstLine[1])
	matrix = []
	for i in xrange(numSubsets):
		matrix.append([])
		line = lines[i + 1]
		parts = line.split()
		#data = raw_input()
		#print len(parts)
		if len(parts) != numItems:
			print "Each line should consist of %d" %numItems + " 0 or 1"
			return 1
		for j in range(numItems):
			#print data[j]
			if parts[j] not in ['0','1']:
				print "Wrong input"
				return 1
			matrix[i].append(parts[j])
			
	t = Table(numItems , numSubsets , matrix)
	#t.greedyAlgo1()
	#print t.answer
	#t.greedyAlgo2()
	#print t.answer
	t.greedyAlgo3()
	print t.answer
	#print t
	return 0
	

if __name__ == '__main__':
	#print sys.argv
	if len(sys.argv) <= 1:
		print "R u an idiot?"
	else:
		fileLocation = sys.argv[1].strip()
		inputDataFile = open(fileLocation,"r")
		inputData = ''.join(inputDataFile.readlines())
		inputDataFile.close()
		main(inputData)
