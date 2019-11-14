
def checkIsWeired(n):
    if n%2 != 0:
        print("Weird")
    elif (n%2 == 0) and (n in range(2,6)) :
        print("Not Weird")
    elif (n%2 == 0) and (n in range(6,21)) :
        print("Weird")
    elif (n%2 == 0) and (n > 20):
        print("Not Weird")
	
def calcUtil(a,b):
	print(str(a+b))
	print(str(a-b))
	print(str(a*b))

def calcUtil1(a,b):
	print(str(a//b)) #integer division
	print(str(a/b)) #floating division
	
def getNsqr(n):
	for i in range(0,n):
		print(i*i)

def is_leap(year):
	leap=False
	if (year%4 == 0) and (year%400==0 or year%100!=0): 
		leap=True
	return leap


# def printWithoutAnyFunction(n):

#print(*range(1, int(input())+1), sep='') # Printing the numbers without any print statement

#List comprehension 
# listA=[ x for x in range(1,10) if x%2 == 0 ] 
# listB=[ "Even" if x%2==0 else "Odd"  for x in range(11) ]
# print(listA)
# print(listB)

# List comprehension 
# x = int ( raw_input()) 
# y = int ( raw_input()) 
# z = int ( raw_input()) 

# n = int ( raw_input()) 
# # ar = [] 
# # p = 0 
# # for i in range ( x + 1 ) : 
# # 	for j in range( y + 1): 
# # 		if i+j != n: 
# # 			ar.append([]) 
# # 			ar[p] = [ i , j ] 
# # 			p+=1 
# # print ar 


# arr =[ [i,j,k] for i in range(x+1) for j in range (y+1) for k in range(z+1) if i+j+k!=n ]

# print(arr)
# print(len(arr))



# find the duplicate

def removeDuplicate(arr):
	print(arr)
	final_list=[]
	for x in arr:
		if x not in final_list:
			final_list.append(x)
	print(final_list)
	return final_list

print(max(removeDuplicate([1,2,33,33,3])))













































# checkIfWeired(3)
# checkIsWeired(18)
#calcUtil(3,2)
# getNsqr(5)
# print(is_leap(2000))
# print(1800%400)
# print(1800%100)
# print(printWithoutAnyFunction(3))

# if __name__ == '__main__':
#     a = int(raw_input())
#     b = int(raw_input())


# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

# https://docs.python.org/3/reference/expressions.html#calls

#https://www.programiz.com/python-programming/list-comprehension