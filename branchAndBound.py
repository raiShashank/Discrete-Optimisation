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
		
	def branchAndBound(self,current_value , capacity , max_possible , item):
		if item == self.num_items or capacity == 0:
			if current_value > self.maxValue:
				self.maxValue = current_value	#self.maxValue stores d tentative soln,u change it only when u find another probable soln i.e capacity = 0 or all items r considered
			return 0
		if max_possible <= self.maxValue:		#which is up nd which below doesn't make any difference since whichever is true will end d curreent recursion
			return 0
		self.recursion += 1
		if capacity - self.weights[item] >= 0:
			self.branchAndBound(current_value + self.values[item] , capacity - self.weights[item] , max_possible , item + 1)	#taken d item
		self.branchAndBound(current_value , capacity  , max_possible - self.values[item] , item + 1)					#not taken d item, since
		#though dere is no error but get into dis habit dat every part of fn shd return if one part returns,i.e here since base case has return statement,other branches shd also have ,but here dat wd hav been wrong since I want d control 2 come nd execute d 2nd fn call outside if,dose return statements were just 2 stop recursing further down, here d object's attributes r modified hence no need 2 return a useful value
values = [45,48,35]
weights = [5,8,3]
capacity = 10
l = LinearEqn(values,weights , capacity)
l.branchAndBound(0 , capacity , sum(values) , 0)
print l.maxValue
print l.recursion
