# String Formatting and substitution 


def generateFormattedMsg(name,order,amount):
	if (len(name)==len(order)==len(amount)):
		i=0
		for t in name:
			msg = m.format(t,order[i],amount[i])
			print(msg)
			i+=1
	else:
		print("Oops!! Some sort of error errors")
	


#=========================================================================

# list for argumnts
list_0=["Bob","Alice", "Tony"]
list_1=["Pizza", "burger", "Hot_magrill"]
list_2=[23,85,100]


#Sample message with argument based formatting

m = """Hello {0}!
How's your doing, ur order for {1}
is one the way.
Your total bill will ${2}
Thankyou!!
"""

print("Generating custom message for each person....\n")
	

generateFormattedMsg(list_0,list_1,list_2)
