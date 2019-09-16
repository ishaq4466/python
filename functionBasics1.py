# conditions, loops and List

#funtion checking whether input string is an integer or not
def isnum(x):
	if x.isdigit() == True:
		return int(x)
	else:
		return x

#Getting the list elements from the user
def getElement(n):
	j = 0
	while n > j:
	 list1.append(isnum(input()))
	 j = j + 1

# Seperating the string elements and popping it from the orignal list
def pop(lst):
	x = 0
	for t in lst:
		if isinstance(t, str) == True:
			strlements.append(t)
			lst.pop(x) 
		x+=1
 




#==============================================================================#
#list1=['sdnasd','ashasjdh',5454,54]
list1=[]
noe = int(input("Enter the number of elements you want in list: "))
print("Start entering the list elements")

getElement(noe)

list2 = list1

print("Original list: "+str(list2))

numlements=[]
strlements=[]

# Seperating the integers and Strings from the list1

#poping of list elements pop(list1)

#pop(list1)

for t in list1:
	if isinstance(t, int) == True:
		numlements.append(t)
	elif isinstance(t, str) == True:
		strlements.append(t)

print("")

print("Ineger elements list: "+str(numlements))
print("String elements list: "+str(strlements))
#print("Integer elements list: "+str(list1))