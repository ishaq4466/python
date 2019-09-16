# Use of Funtions, List , loops

def mylistfilter(listy):
	num=[]
	for t in listy:
		if (isinstance(t, int) or isinstance(t, float)) == True:
			num.append(t)
	return num

def mysum(listx):
	s=0
	for t in listx:
		s+=t
	return s

def avsum(numlist):
	s=avg=0
	numlist = mylistfilter(list_a)
	s=mysum(numlist)
	avg = s/len(numlist)
	return s,avg, numlist
#======================================================================#
# Calculation of sum and averages of int and floats in given List

list_a =["Hello",233,84.37, 9.38, "sdd", 73, "justin", 45,78]
print(list_a)

#FUNCTION RETURNING 3 VALUES 

my_sum, average, numlist = avsum(list_a)

print("Numbers in list:"+str(numlist))
print("Sum of all numbers in list: "+str(my_sum))
print("Average is "+str(average))