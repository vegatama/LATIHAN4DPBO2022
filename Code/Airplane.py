from Vehicle import Vehicle

class Airplane(Vehicle):
	# private atribute 
	__type = ""
	__age = 0
	__wingsLength = 0

	# constructor
	def __init__(self, type, age, wingsLength):
		self.__type = type
		self.__age = age
		self.__wingsLength = wingsLength

	# getter/setter
	def settype(self, type):
		self.__type = type

	def gettype(self):
		return self.__type

	def setage(self, age):
		self.__age = age

	def getage(self):
		return self.__age
	
	def setwingsLength(self, wingsLength):
		self.__wingsLength = wingsLength

	def getwingsLength(self):
		return self.__wingsLength

	# method
	def printAirplane(self):
		print("Airplane type : " + str(self.__type))
		print("Airplane age : " + str(self.__age))
		print("Airplane wingsLength : " + str(self.__wingsLength))
	
