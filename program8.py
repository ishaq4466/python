#Clases, Methods and Instanstiation

class Animal():
	nameofanimal =""
	typeofanimal = "domestic"
	noise = "Grunt"


#Dog class is extending the Animal class
class Dog(Animal):
	name = ""
	color =""
	breed = ""
	def getData(self):
		return self.name,self.color,self.breed
	
	def setData(self,l):
		self.name = l[0]
		self.color = l[1]
		self.breed = l[2]
		self.noise = l[3]
		self.nameofanimal = l[4]		

#making fuction act as a variable
	@property
	def showData(self):
		dogDetail = """The animal is {4} and his name is {0} which is of {1}
breed  and color of the {4} is {2} it makes {3} noise"""
		detail = dogDetail.format(self.name,self.color,self.breed,self.noise,self.nameofanimal)
		print(detail)

#Getting the animal name
def animal(l):
	if isinstance(l, Dog):
		return "Dog"
	else:
		return "to be known"

d1 = Dog()
list_a = ["Rusk", "Seberian", "Brown", "Barking"]
list_a.append(animal(d1))
d1.setData(list_a)
d1.showData
#print(type(d1))


