#I will first implement sudoku using bruteforce
#0 in cells denote that dey have not yet been filled
class Sudoku:
	def __init__(self,board,dimension = 9):
		"""
			board : a 9 X 9 grid
			prespecified : list of 9 lists : each list contains a tuple
		"""
		self.board = board
		self.dimension = dimension
		self.stack = []
		self.solution = 0
		self.recursion = 0
	def __str__(self):
		answer = ""
		for i in xrange(self.dimension):
			answer += str(self.board[i])
			answer += "\n"
		return answer
		
	def guess(self,row,col):
		#print "#############################################################\t New Recursion"
		#print "-----------------B4 makin guess---------------------"
		#print self
		self.recursion += 1
		#print self.recursion
		#if self.recursion % 1000 == 0:
		print "After %d recursions " % self.recursion
		print self
		found = False
		i = 0
		j = 0
		while i < self.dimension:
			#if i != row:
			j = 0
			while j < self.dimension:
				if self.board[i][j] != 0:
					pass
				else:
					found = True
					break
				j += 1
			if found == True:		# I have found i,j st board[i][j] == 0
				break
			i += 1
		if found == False:		# all further rows nd cols r occupied
			print "Got a solution. Hurray"
			self.solution += 1
			return 0
		for choice in xrange(1,self.dimension + 1):
			self.board[i][j] = choice
			#print "-----------------After makin guess---------------------"
			#print self
			if self.satisfyConstraint(i,j) == True:		#if things were ok tilll now den after making dis entry only dis row,col or sub-matrix might go wrong
				if j < self.dimension - 1:
					if self.guess(i,j + 1) == 0:
						return 0
				elif i < self.dimension - 1:
					if self.guess(i + 1, 0) == 0:
						return 0
				else:
					print "Got a solution. Hippy"
					self.solution += 1
					return 0
			else:
				self.board[i][j] = 0
				
		return 1
	def satisfyConstraint(self,row,col):
		count = 0
		choice  = self.board[row][col]
		#print choice
		#print self.board[row]
		for j in xrange(self.dimension):
			if choice == self.board[row][j]:
				count += 1
				#print count
				if count > 1:
					#print "-------------------------Wrong Guess---------------------------"
					return False
		for i in xrange(self.dimension):
			if choice == self.board[i][col]:
				count += 1
				if count > 2:
					#print "-------------------------Wrong Guess---------------------------"
					return False
		k = int(row/3)
		l = int(col/3)
		k = k * 3
		l = l * 3
		for i in xrange(k,k+3):
			for j in xrange(l,l+3):
				if choice == self.board[i][j]:
					count += 1
					if count > 3:
						#print "-------------------------Wrong Guess---------------------------"
						return False
		#print "-------------------------Right Guess---------------------------"
		return True
					

				
def intify(x):
	#print "Hi"
	#for i in lst:
	try:
		return int(x)
	except ValueError:
		return x
	#	return lst
def solveIt(inputData):
	lines = inputData.split('\n')
	dimension = int(lines[0])
	board = []
	for i in xrange(1,dimension + 1):
		row = lines[i].split()
		j = 0
		for x in row:
			row[j] = intify(x)
			j += 1
		#print row
		if len(row) != dimension:
			print "Each row must contain %d elements" % dimension
			return 1
		for item in row:
			if item not in range(dimension + 1):
				print "Element in %d th row must be between %d and %d" % (i,1,dimension)
				return 1
		board.append(row)
	s = Sudoku(board)
	s.guess(0,0)
	print "No. of solutions = \t",s.solution
	#print s
	
		
import sys
def main():
	if len(sys.argv) < 2:
		print "Give a filename which contains configuration of sudoku"
	else:
		fileLocation = sys.argv[1].strip()
		inputDataFile = open(fileLocation,'r')
		inputData = ''.join(inputDataFile.readlines())
		inputDataFile.close()
		solveIt(inputData)
	
	
if __name__ == '__main__':
	main()
