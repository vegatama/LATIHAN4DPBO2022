class Job:
	# private atribute 
	__NIP = 0
	__companyName = ""
	__position = ""

	# constructor
	def __init__(self, NIP, companyName, position):
		self.__NIP = NIP
		self.__companyName = companyName
		self.__position = position

	# getter/setter
	def setNIP(self, NIP):
		self.__NIP = NIP

	def getNIP(self):
		return self.__NIP

	def setcompanyName(self, companyName):
		self.__companyName = companyName

	def getcompanyName(self):
		return self.__companyName
	
	def setposition(self, position):
		self.__position = position

	def getposition(self):
		return self.__position

	# method
	def printJob(self):
		print("Job NIP : " + str(self.__NIP))
		print("Job companyName : " + str(self.__companyName))
		print("Job position : " + str(self.__position))
	
