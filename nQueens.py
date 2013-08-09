# queen : 2
#allowed places : 0
import pylab
class Chess(object):
	def __init__(self,dimension):
		self.dimension = dimension
		self.solution = 0
		self.recursion = 0
		self.solutionSet = []
		#self.board = [[0] * dimension for i in xrange(dimension)]
		self.board = []
		for i in xrange(self.dimension):
			self.board.append([])
			for j in xrange(self.dimension):
				self.board[i].append(0)
		
	def __str__(self):
		#chessBoard = pylab.array(self.board)
		#return str(chessBoard)
		answer = ''
		for i in self.board:
			answer += str(i)
			answer += '\n'
		return answer
	def play(self,chess,row,col):
		"""
			chess: configuration of the board rite now
		"""
		self.recursion += 1
		X = col
		Y = row
		#chess[Y][X] = 2
		self.putConstraint(chess,row,col)
		#print pylab.array(chess)
		#print pylab.array(chess)
		i = 0 
		j = 0
		repeat = False
		while not repeat:
			repeat = True
			sigma = 0
			while i < self.dimension:
				sigma = 0
				#print chess[x]
				#print type(chess[x])
				#print type(chess[x][0])
				for j in xrange(self.dimension):	#chess[i] is a complete row
					sigma += chess[i][j]
				if sigma == self.dimension:		# all places with 1, ideally v want one queen nd rest all 1.i.e sum = self.dimension + 1
					print "not possible"
					return 1
				if sigma == self.dimension - 1:
					
					for j in xrange(self.dimension):
						if chess[i][j] == 0:
							repeat = False
							#chess[i][j] = 2
							self.putConstraint(chess,i,j)		#i is row no. j is col no.
				
				i += 1
			j = 0
			sigma = 0
			while j < self.dimension:
				sigma = 0
				for i in xrange(self.dimension):
					sigma += chess[i][j]		#for a given col j I want 2 find sun of values in all d rows
				if sigma == self.dimension:
					print "not possible"
					return 1
				if sigma == self.dimension - 1:
					repeat = False
					for i in xrange(self.dimension):
						if chess[i][j] == 0:
							#chess[i][j] = 2
							self.putConstraint(chess,i,j)
				j += 1
				
		# Previous guess for Queen was made in row row, guess fr a suitable place for queen in row + 1
		count = 1
		for i in chess:
			#print i
			if sum(i) != self.dimension + 1:
				count = 0
				break
		if count == 1:
			#self.board = chess
			#print self
			self.encode(chess)
			#self.solution += 1
			return 0
		i = row + 1
		while i  < self.dimension:
			#print i
			#if j < self.dimension:
			if sum(chess[i]) == self.dimension + 1:	#d next row already contains a queen
				i += 1
			else:
				break
		if i < self.dimension:
			for j in xrange(self.dimension):
				if chess[i][j] == 0:
					#count += 1
					copy = self.replicate(chess)
					#print copy == chess
					#print copy is chess
					self.play(copy,i,j)		#i denotes d row nd j denotes d column
					#print "After returning back"
					#print pylab.array(chess)
	def encode(self,chess)	:
		possibleAnswer = []
		for i in xrange(self.dimension):
			for j in xrange(self.dimension):
				if chess[i][j] == 2:
					possibleAnswer.append((i,j))
					break							#since it is a possible configuration,hence dere can only b 1 queen in every row
					
		if possibleAnswer not in self.solutionSet:
			self.solutionSet.append(possibleAnswer)
			self.solution += 1
	def printSolutions(self):
		i = 0
		while i < self.solution:
			print self.decode(self.solutionSet[i])
			i += 1
			
	def decode(self,coordinates):
		"""
			coordinates : list of tuples(row,col) which should be 1
		"""
		ans = Chess(len(coordinates))
		for point in coordinates:
			ans.board[point[0]][point[1]] = 2
		return ans
		
	def replicate(self, chess)	:
		copy = []
		for i in chess:
			copy.append(i[:])
		return copy
	def putConstraint(self , chess , row , col):
		y = row 
		x = col
		i = j = 0
		#print row,col
		# adding constraint to row nd column
		while i < self.dimension:
			chess[i][x] = 1		#col
			chess[y][i] = 1		#row
			i += 1
		## adding constraint to left diagonal assume it is represented by line y = x + c since slope = 1 
		#c = y - x
		#xIntercept = -1 * c
		#i = 0
		#while i <= xIntercept :
			#chess[xIntercept - i][i] = 1
			#i += 1
		## adding constraint to right diagonal assume it is represented by line y = -x + c since slope = -1 
		#c = x + y
		#yIntercept = c
		#i = 0
		#while i < self.dimension - yIntercept:
			#chess[i][yIntercept + i] = 1
			#i += 1
		i = 0
		while row + i < self.dimension and col + i < self.dimension:
			chess[row + i][col + i] = 1
			i += 1
		i = 0
		while row - i >= 0 and col + i < self.dimension:
			chess[row - i][col + i] = 1	
			i += 1
		i = 0	
		while row + i < self.dimension and col - i >= 0:
			chess[row + i][col - i] = 1
			i += 1
		i = 0	
		while row - i >= 0 and col + i < self.dimension:
			chess[row - i][col + i] = 1
			i += 1
			
		# dat plce where u hav put queen is overwritten by 1, it is guaranteed dat only one queen is overwritten,it is guaranteed else dis new queen 
		# must not hav come in d first place
		chess[row][col] = 2		#want 2 go 2 chess[y] row nd col no. x of dis row
		
c = Chess(10)
#print c
col = 0
limit = c.dimension % 2

while col < c.dimension:	#in d play function, for every greater row I m checking fr every column.hence I have made here sure dat 1st col also 
	copy = c.replicate(c.board)
	c.play(copy,0,col)	#keeps changing
	col += 1
#if c.dimension % 2 == 1:
	#copy = c.replicate(c.board)
	#c.play(copy,0,col)
#print c
c.printSolutions()
if c.solution == 0:
	print "not possible on  a chessboard with dimension  %d" % c.dimension
else:
	print "No. of solutions = \t", c.solution
print "No. of recursion",c.recursion

