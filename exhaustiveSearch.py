class LinearEqn(object):
	def __init__(self,values,weights,capacity):
		"""values and weights : list of ints
			capacity :an int
		"""
		self.values = values
		self.weights = weights
		self.capacity = capacity
		self.recursion = 0
		
	def exhaust(self,sampleSpace , capacity):
		"""
			sampleSpace : a list [0,1,2] denotes dat dere r 3 items [1,2] denotes dat dere r 2 objects remaining, 2 b particular 2nd and 3rd
			capacity : int denotes how much more weigty can b put in d bag
		"""
		if capacity <= 0 or not sampleSpace:
			return 0
		print sampleSpace , "\t" , capacity
		item = sampleSpace.pop(0)
		self.recursion += 1
		
		if capacity - self.weights[item] >= 0:
			taken = self.values[item] + self.exhaust(sampleSpace[:] , capacity - self.weights[item])
		else:
			return self.exhaust(sampleSpace[:] , capacity)
		not_taken = self.exhaust(sampleSpace[:] , capacity)
		ans = max(taken , not_taken)
		return ans
		
values = [45,48,35]
weights = [5,8,2]
capacity = 10
l = LinearEqn(values,weights , capacity)
print l.exhaust([0,1,2] , capacity )
print l.recursion
