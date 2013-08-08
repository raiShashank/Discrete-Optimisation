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
			self.answer.append(i)
			items = self.setToItems[i]
			for item in items:
				if remainingItem[item] > 0:
					remainingItem[item] -= 1
				
			s = sum(remainingItem.values())
			if s == 0:
				break
			
			
		
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
	t.greedyAlgo1()
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
