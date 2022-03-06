class Vehicle:
	# private atribute 
	__fuelType = ""
	__maxPassengers = 0

	# constructor
	def __init__(self, fuelType, maxPassengers):
		self.__fuelType = fuelType
		self.__maxPassengers = maxPassengers

	# getter/setter
	def setfuelType(self, fuelType):
		self.__fuelType = fuelType

	def getfuelType(self):
		return self.__fuelType

	def setmaxPassengers(self, maxPassengers):
		self.__maxPassengers = maxPassengers

	def getmaxPassengers(self):
		return self.__maxPassengers

	# method
	def Move(self):
		print("Vehicle is moving ->->->")

	def printVehicle(self):
		print("Vehicle fuelType : " + str(self.__fuelType))
		print("Vehicle maxPassengers : " + str(self.__maxPassengers))
