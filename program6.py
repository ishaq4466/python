# String Formatting and substitution 


def generateFormattedMsg(mydict):
	if (len(mydict["Name"])==len(mydict["Favroute"])==len(mydict["Age"])):
		i=0
		for t in mydict["Name"]:
			msg = m.format(t,mydict["Favroute"][i],mydict["Age"][i])
			print(msg)
			i+=1
	else:
		print("Oops!! Some sort of error, check the list")
	


#=========================================================================

# list for argumnts
list_0=["Bob","Alice", "Tony"]
list_1=["Pizza", "burger", "Hot_magrill"]
list_2=[23,85,100]
mydict={"Name":list_0,"Favroute":list_1,"Age":list_2}


#Order Sample message with argument based formatting

m = """Hello {0}!
How's your doing, ur order for {1}
is one the way.
Your total bill will ${2}
Thankyou!!
"""

print("Generating custom message for each person....\n")
	
#Passing a dictionary instead of lists

generateFormattedMsg(mydict)
