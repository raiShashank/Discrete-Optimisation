# queen : 2
#allowed places : 0
import pylab
class Chess(object):
	def __init__(self,dimension):
		"""
			row : a list of lists , each list stores values possible for that column.It is basically a decision variable fr my model.If d list contains
					just one value, gud lse make a choice ,while making choice, I'll send copy of d row frm ith list ,i.e row[i:] since I won't
					get any benefit by changing values of possible values fr earlier lists since there I have already made the choice
		"""
		self.dimension = dimension
		self.solution = 0
		self.recursion = 0
		self.solutionSet = []
		self.board = [[0] * dimension for i in xrange(dimension)]
		self.row = []
		for i in xrange(self.dimension):
			self.row.append([])
			for j in xrange(self.dimension):
				self.row[i].append(j)
			self.row[i].append(self.dimension * self.dimension + self.dimension)	# no. of possible values dese decision variables can take
			self.row[i].append("False")				# 0 denots dat queen has not been put in dat column
	def __str__(self):
		#chessBoard = pylab.array(self.board)
		#return str(chessBoard)
		answer = ''
		for i in self.row:
			answer += str(i)
			answer += '\n'
		return answer
	# c.choice(0,c.row[:] , 0)	
	def choice(self,colNo , row , choice , possibleAnswer):
		"""
			choice : row no where we decided 2 plzce d queen in colNo
			colNo : an int [0, self.dimension) denotes in which column do I have 2 make d choice
			row : list of lists but colNo  is d first column here i.e row[0] refers to self.row[colNo - 1]	(start column is 0) so that when I backtrack
					in d fn which called dis invokation, I don't have any effect of dese calls
		"""
		self.prune(colNo , row , choice)
		row[colNo][-1] = "True"
		
		possibleAnswer.append((choice,colNo))
		#self.board[choice][colNo] = 2
		#for h in xrange(self.dimension):
		#	print self.board[h]
		#print 
		#for h in xrange(self.dimension):
						#print row[h]
		#print "-------------------------"
		repeat = False
		#i = 0
		#while i < 2:
		while not repeat:
		
			repeat = True
			for i in xrange(colNo + 1,self.dimension):
				if row[i][-2] == self.dimension * self.dimension:
					print "Not Possible"
					return 1
				if row[i][-2] == self.dimension * self.dimension + 1 and row[i][-1] == "False":
					rowNo = row[i][0]	#rowNo is a list containg singleton row no. in which d queen can b put, D queen in ith col has 2 b put in dis row
					self.prune(i , row , rowNo)
					row[i][-1] = "True"
					possibleAnswer.append((rowNo,i))
					#self.board[rowNo][i] = 2
					#for h in xrange(self.dimension):
					#	print self.board[h]
					#print 
					#for h in xrange(self.dimension):
						#print row[h]
					#print
					repeat = False
					
			#i += 1
		#print "Shashank"
		count = 0
		for i in xrange(colNo + 1, self.dimension):
			if row[i][-1] == "True":
				count += 1
				continue
			else:
				break
		if count == self.dimension - colNo - 1:		# all cols have got a queen each
			print "Got a solution"
			if possibleAnswer not in self.solutionSet:
				self.solutionSet.append(possibleAnswer)
				self.solution += 1
			return 0
		if colNo + 1 + count < self.dimension:
			for rowNo in row[colNo + 1 + count][:-2]:
				copy = self.replicate(row,0)
				self.choice(colNo + 1 + count, copy, rowNo , possibleAnswer[:])
	def prune(self,colNo , row , choice)	:
		#i = 0
		for i in xrange(colNo + 1,self.dimension):
			if choice in row[i]:
				row[i].remove(choice)
				row[i][-2] -= 1
			if choice - (i - colNo) in row[i]:
				row[i].remove(choice - (i - colNo))
				row[i][-2] -= 1
			if choice + (i - colNo) in row[i]:
				row[i].remove(choice + (i - colNo))
				row[i][-2] -= 1
	def replicate(self, row , colNo)	:
		copy = []
		#i = 0
		for i in xrange(colNo,self.dimension):
			copy.append(row[i][:])
			#i += 1
		return copy
	
		
c = Chess(9)
possibleAnswer = []
print c
for rowNo in c.row[0][:-2]:
	copy = c.replicate(c.row,0)
	c.choice(0,copy,rowNo,[])
#col = 0
#limit = c.dimension % 2

#while col < c.dimension:	#in d play function, for every greater row I m checking fr every column.hence I have made here sure dat 1st col also 
	#copy = c.replicate(c.board)
	#c.play(copy,0,col)	#keeps changing
	#col += 1
##if c.dimension % 2 == 1:
	##copy = c.replicate(c.board)
	##c.play(copy,0,col)
##print c
#c.printSolutions()
#if c.solution == 0:
	#print "not possible on  a chessboard with dimension  %d" % c.dimension
#else:
	#print "No. of solutions = \t", c.solution
#print "No. of recursion",c.recursion
print "No. of solutions = \t", c.solution
