
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

print(*range(1, int(input())+1), sep='') # Printing the numbers without any print statement
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


