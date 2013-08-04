class Node(object):
	def __init__(self ,value , capacity , maxPossible , item):
		"""
			value : current value of d node
			capacity : remaining capacity of d bag
			maxPossible : using remaining items what is d best dat can be filled, 
			item : denotes itemNo. lik 2 which means dat maxPossible shd now focus on items from 2 onwards
		"""
		self.value = value
		self.capacity = capacity
		self.maxPossible = maxPossible
		self.item = item
	def __str__(self):
		return "Value = %d capacity = %d MaxPossible = %d" % (self.value , self.capacity , self.maxPossible)

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
		self.nodeList = []
		bestPossible = 0
	def checkSolution(self , node):
		"""
			if it is d last node on d branch den it deletes all othere small maxPossible nodes
		"""
		item = node.item
		if item == self.num_items or node.capacity == 0:		#in d subsequent code I am expanding dis node,hence i shd make dis check 
			if node.value > self.maxValue:
				self.maxValue = node.value
			newNodeList = []
			for nod in self.nodeList:
				if nod.maxPossible > self.maxValue:
					newNodeList.append(nod)		#dere is no need 2 put dis particular node back in d nodeList,hence no >=
					
			self.nodeList = newNodeList
			return True
		
	def bestSearch(self , node):
		"""
			node : an object of class Node
		"""
		print "\nActine Node for this round:\t",node,"\n"
		item = node.item
		if item == self.num_items or node.capacity == 0:		#in d subsequent code I am expanding dis node,hence i shd make dis check 
			if node.value > self.maxValue:
				self.maxValue = node.value
			newNodeList = []
			for nod in self.nodeList:
				if nod.maxPossible > self.maxValue:
					newNodeList.append(nod)		#dere is no need 2 put dis particular node back in d nodeList,hence no >=
					
			self.nodeList = newNodeList
			
			if not self.nodeList:	#check if d nodeList is empty(False) in which case I have d final ans
				return 0
		
		self.recursion += 1
		
		value = node.value + self.values[item]
		capacity = node.capacity - self.weights[item]
		if capacity >= 0:
			print capacity 
			maxPossible = node.maxPossible
			
			if self.checkSolution(Node(value , capacity , maxPossible , item + 1)):
				pass
			else:
				newNodeList = []
				for nod in self.nodeList:
					if nod.maxPossible < maxPossible:
						newNodeList.append(nod)
						
				newNodeList.append(Node(value , capacity , maxPossible , item + 1))
				
				for nod in self.nodeList:
					if nod.maxPossible >= maxPossible:
						newNodeList.append(nod)
						
				self.nodeList = newNodeList	
			
		
		maxPossible = node.maxPossible - self.values[item]
		
		if self.checkSolution(Node(node.value , node.capacity , maxPossible , item + 1)):
				pass
		else:
			newNodeList = []
			for nod in self.nodeList:
				if nod.maxPossible < maxPossible:
					newNodeList.append(nod)
					
			newNodeList.append(Node(node.value , node.capacity , maxPossible , item + 1))
			
			for nod in self.nodeList:
				if nod.maxPossible >= maxPossible:
					newNodeList.append(nod)	
			
			self.nodeList = newNodeList
		
		for nod in self.nodeList:
			print nod
			
		if self.nodeList :
			bestNode = self.nodeList.pop()
			self.bestSearch(bestNode)	#since d recursive call is d last thing hence when any one returns , all will return
		else:
			return 0

values = [45,48,35]
weights = [5,8,3]
capacity = 10
l = LinearEqn(values , weights , capacity)
l.bestSearch(Node(0 , 10 , sum(values) , 0 ))
print l.maxValue
print l.recursion
