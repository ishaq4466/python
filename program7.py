#Clases, Methods and Instanstiation
class Dog():
	name = ""
	color =""
	breed = ""
	def getData(self):
		return self.name,self.color,self.breed

	def setData(self,l):
		self.name = l[0]
		self.color = l[1]
		self.breed = l[2]		

	def showData(self):
		dogDetail = """The dog name is {0} which is of {1}
breed  and color of the dog is {2} """
		detail = dogDetail.format(self.name,self.color,self.breed)
		print(detail)

list_a = ["Rusk", "Seberian", "Brown"]
list_b = ["Husk", "Seberian-Green", "White"]
dog1 = Dog()
dog1.setData(list_a)
dog1.showData()

dog2 = dog1
print("")
dog2.showData()
print("")
dog2.setData(list_b)
dog2.showData()