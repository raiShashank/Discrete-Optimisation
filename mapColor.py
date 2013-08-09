class Map(object):
	def __init__(self,colorSet,countrySet):
		self.colrSet = colorSet
		self.countrySet = countrySet
		self.color = {}
	def printNeighbours(self):
		for country in self.countrySet:
			print country.getName(), ":",
			country.printNeighbours()
class Country(object):
	def __init__(self,name ):
		"""
			neighbourSet : list denoting list of neighbours of the country
		"""
		self.name = name
	def setNeighbours(self,neighbourSet):
		"""
			neighbourSet : list denoting list of names neighbours of the country
		"""
		self.neighbourSet = neighbourSet
	def printNeighbours(self):
		for country in self.neighbourSet:
			print country.name,
		print	
	def getName(self):
		return self.name
		
Belgium = Country("Belgium")
Denmark = Country("Denmark")
France = Country("France")
Germany = Country("Germany")
Netherlands = Country("Netherlands")
Luxemburg = Country("Luxemburg")

Belgium.setNeighbours([France,Luxemburg,Germany,Netherlands])
Denmark.setNeighbours([Germany])
France.setNeighbours([Belgium,Luxemburg])
Germany.setNeighbours([Belgium,Denmark,Luxemburg,Netherlands])
Luxemburg.setNeighbours([Belgium,France,Germany])
Netherlands.setNeighbours([Belgium,Germany])

countrySet = [Belgium,Denmark,France,Germany,Luxemburg,Netherlands]
colorSet = ["Black","Yellow","Blue","Brown"]

Europe = Map(colorSet,countrySet)
Europe.printNeighbours()
