from Job import Job

class Driver(Job):
	# private atribute 
	__lisenceID = 0
	__activeUntil = ""
	__vehicleType = ""

	# constructor
	def __init__(self, lisenceID, activeUntil, vehicleType):
		self.__lisenceID = lisenceID
		self.__activeUntil = activeUntil
		self.__vehicleType = vehicleType

	# getter/setter
	def setlisenceID(self, lisenceID):
		self.__lisenceID = lisenceID

	def getlisenceID(self):
		return self.__lisenceID

	def setactiveUntil(self, activeUntil):
		self.__activeUntil = activeUntil

	def getactiveUntil(self):
		return self.__activeUntil
	
	def setvehicleType(self, vehicleType):
		self.__vehicleType = vehicleType

	def getvehicleType(self):
		return self.__vehicleType

	# method
	def printDriver(self):
		print("Driver lisenceID : " + str(self.__lisenceID))
		print("Driver activeUntil : " + str(self.__activeUntil))
		print("Driver vehicleType : " + str(self.__vehicleType))
	
