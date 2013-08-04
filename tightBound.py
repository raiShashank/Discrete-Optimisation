class LinearEqn(object):
	def __init__(self,values,weights,capacity):
		"""values and weights : list of ints
			capacity :an int
		"""
		self.values = values
		self.weights = weights
		self.capacity = capacity
		self.recursion = 0
		self.maxValue = 0
		self.num_items = len(self.values)
		
	def calcTightBound(self , capacity , itemNotTaken):
		"""
			capacity : int denoting current capacity of node/bag
			values,weights : list of ints
		"""
		maxPossible = 0
		values = []
		weights = []
		for item in xrange(self.num_items):
			if item not in itemNotTaken:
				values.append(self.values[item])
				weights.append(self.weights[item])
		
		i = 0
		valuePerWeight = {}
		while i < len(values):
			valuePerWeight[float(values[i]) / weights[i]] = (weights[i],values[i])
			i += 1
		
		#print valuePerWeight
		valuable = sorted(valuePerWeight, reverse = True)
		#print valuable
		for elem in valuable:
			
			if valuePerWeight[elem][0] <= capacity:
				capacity -= valuePerWeight[elem][0]
				maxPossible += valuePerWeight[elem][1]
			else:
				maxPossible += capacity * elem
				capacity = 0
				break
		print maxPossible
		return maxPossible
		
	def tightBound(self , current_value , capacity, itemNotTaken , maxPossible,item):
		if maxPossible <= self.maxValue:
			return 0
		if item == self.num_items or capacity == 0:
			if current_value > self.maxValue:
				self.maxValue = current_value
				return 0
				
		self.recursion += 1
		#print self.recursion,"\t",current_value,"\t",capacity,"\t",maxPossible
		if capacity - self.weights[item] >= 0:
			self.tightBound(current_value + self.values[item] , capacity - self.weights[item] , itemNotTaken[:] , maxPossible,item + 1)	#taken d item
		
		itemNotTaken.append(item)
		maxPossible = self.calcTightBound(self.capacity , itemNotTaken)
		self.tightBound(current_value , capacity , itemNotTaken[:] , maxPossible,item +1 )

values = [45,48,35]
weights = [5,8,2]
capacity = 10
l = LinearEqn(values , weights , capacity)
maxPossible = l.calcTightBound(capacity , [] )
l.tightBound(0 , capacity , [] , maxPossible , 0)
print l.maxValue
print l.recursion
