class Person:
	# private atribute 
	__NIK = 0
	__Name = ""
	__Gender = ""

	# constructor
	def __init__(self, NIK, Name, Gender):
		self.__NIK = NIK
		self.__Name = Name
		self.__Gender = Gender

	# getter/setter
	def setNIK(self, NIK):
		self.__NIK = NIK

	def getNIK(self):
		return self.__NIK

	def setName(self, Name):
		self.__Name = Name

	def getName(self):
		return self.__Name
	
	def setGender(self, Gender):
		self.__Gender = Gender

	def getGender(self):
		return self.__Gender

	# method
	def sleep(self):
		print(str(self.__Name) + "is sleeping Zzz")
	
	def printPerson(self):
		print("Person NIK : " + str(self.__NIK))
		print("Person Name : " + str(self.__Name))
		print("Person Gender : " + str(self.__Gender))
	
