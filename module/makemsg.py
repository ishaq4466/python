#Classes

class UserMsg():
	#usrdetail is a list of dictionary 
	usrdetail=[]
	msg = []
	basemsg="""Hii {0}, Thankyou for ordering {1}
your order is on the way. Just making remember to you,yours 
order bill will {2}$. 
Thanyou!!!"""
	
	def addOrder(self,name=None,item=None,amount=None):
		usrdict = {"Name":name,
		"Item":item,
		"Amount":amount}
		self.usrdetail.append(usrdict)


	def userMsg(self, name):
		if len(self.usrdetail) is not None:
			for t in self.usrdetail:
				if t["Name"] is name:
					msg = self.basemsg.format(t["Name"],t["Item"],t["Amount"])
					print(msg)
		

	def dispMsg(self,name=None):
		if len(self.usrdetail) is not None and name is None:
			for t in self.usrdetail:
				msg = self.basemsg.format(t["Name"],t["Item"],t["Amount"])
				print(msg)
		else:
			#pass
			self.userMsg(name)


usr1 = UserMsg()
usr1.addOrder("Joe","Iron Fist",1000)
usr1.addOrder("Jo","Iron Fist",15)
usr1.dispMsg("Jo")
#usr1.dispMsg()



