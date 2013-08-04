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
		
	def calcTightBound(self , capacity , start):
		"""
			capacity : int denoting current capacity of node/bag
			values,weights : list of ints
		"""
		maxPossible = 0
		values = self.values[start:]
		weights = self.weights[start:]
		
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
		#print maxPossible
		return maxPossible
		
	def tightBound(self , current_value , capacity, item , maxPossible):
		if maxPossible <= self.maxValue:
			return 0
		if item == self.num_items or capacity == 0:
			if current_value > self.maxValue:
				self.maxValue = current_value
				return 0
				
		self.recursion += 1
		#print self.recursion,"\t",current_value,"\t",capacity,"\t",maxPossible
		if capacity - self.weights[item] >= 0:
			self.tightBound(current_value + self.values[item] , capacity - self.weights[item] , item + 1 , maxPossible)	#taken d item
		
		
		maxPossible = current_value + self.calcTightBound(capacity , item + 1)
		#print maxPossible
		self.tightBound(current_value , capacity , item + 1 , maxPossible )

values = [45,48,35]
weights = [5,8,3]
capacity = 10
l = LinearEqn(values , weights , capacity)
maxPossible = l.calcTightBound(capacity , 0 )
l.tightBound(0 , capacity , 0 , maxPossible)
print l.maxValue
print l.recursion

#look when I am at a node,maxPossible shd mean given dat what has happened till now what is d best dat can b done wid dis bag,I might hav made a 
# wrong choice earlier, but maxPossible shd not show m now dat look wr max can b X(if u had not taken dat item) since I will then make right choice
# in other branch hence I am not losing anything, anyway I can't change whatever I have already done
