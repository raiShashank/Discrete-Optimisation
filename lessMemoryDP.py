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
		
	def newList(self):
		"""
			k : int denotes length of list, all initialized to 0
		"""
		tempList = []
		i = 0
		while i <= self.capacity:
			tempList.append((0,[]))
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
		col2[k][1].append(0)
		for j in xrange(1,self.numItems + 1):		#[1,numItems]
			for k in xrange(1,self.capacity + 1):	#k : capacity [1,capacity]
				if self.weights[j - 1] > k:
					optimalSoln = col1[k][1][:]
					optimalSoln.append(0)
					col2[k] = (col1[k][0],optimalSoln)	#0 denotes dat jth iitem is not taken 2 optimally fill d bag of wt w frm items [1,j]
				else:
					check = cmp(col1[k][0] , self.values[j - 1] + col1[k  - self.weights[j - 1]][0])
					if check >= 0 :		# if > den jth item shd not b included , but if = den dere exists a soln by including as well as by not
						optimalSoln = col1[k][1][:]
						optimalSoln.append(0)
						col2[k] = (col1[k][0] , optimalSoln)	#mind u opt soln 2 fill d bag wid capacity k exists both ways,rite now I can't say anything about d full bag
					else:		#include d jth item
						optimalSoln = col1[k  - self.weights[j - 1]][1][:]
						optimalSoln.append(1)
						col2[k] = (self.values[j - 1] + col1[k  - self.weights[j - 1]][0] , optimalSoln)
			print col2	
			col1 = col2
			col2 = self.newList()
			
		return col1[self.capacity][0],col1[self.capacity][1]
		
values = [45,48,35]
weights = [5,8,3]
capacity = 10
dp = DynamicProgramming(capacity , values , weights)
maxPossible, configuration = dp.dynamicProgramming()
print maxPossible
print configuration
