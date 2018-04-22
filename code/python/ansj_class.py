class Ansj():
	name = ''
	age  = 0
	sex  = 'male'
	def setName(self,name):
		self.name = name
	def getName(self):
		print self.name
	def setAge(self,age):
		self.age = age
	def getAge(self):
		print self.age

ansj=Ansj()
print(ansj.name,ansj.age,ansj.sex)
ansj.setAge(25)
ansj.setName('anshijie')

ansj.getAge()
ansj.getName()