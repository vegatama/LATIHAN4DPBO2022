from Vehicle import Vehicle

class Ship(Vehicle):
	# private atribute 
	__age = 0
	__type = ""
	__countryOfManufacture = ""

	# constructor
	def __init__(self, age, type, countryOfManufacture):
		self.__age = age
		self.__type = type
		self.__countryOfManufacture = countryOfManufacture

	# getter/setter
	def setage(self, age):
		self.__age = age

	def getage(self):
		return self.__age

	def settype(self, type):
		self.__type = type

	def gettype(self):
		return self.__type
	
	def setcountryOfManufacture(self, countryOfManufacture):
		self.__countryOfManufacture = countryOfManufacture

	def getcountryOfManufacture(self):
		return self.__countryOfManufacture

	# method
	def printShip(self):
		print("Ship age : " + str(self.__age))
		print("Ship type : " + str(self.__type))
		print("Ship countryOfManufacture : " + str(self.__countryOfManufacture))
	
