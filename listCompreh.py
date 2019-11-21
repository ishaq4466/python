
# [ expression for items in list ]
arr1=[ x for x in range(0,11) ]

print(arr1)

print([ [i,j] for i in range(0,3) for j in range(0,3) ] )

print([ [i,j]	 if i==j else [0,0,0]  for i in range(0,3) for j in range(0,3) if i==j ] )


# Making a 3x3 matrix

matrixA=[]
rows=3#int(input())
cols=3#int(input())
p=0
# through for loops
for x in range(rows):
	matrixA.append([])
	for y in range(cols):
		# print(y)
		matrixA[p].append(y)
	p+=1
print(matrixA)
# through the list comprehesion
matrixB=[ [y for y in range(cols) ]for x in range(rows)]
# 3x3 identity matrix
# matrixB=[ [ 1 if x==y else 0 for y in range(cols) ] for x in range(rows)]
print(matrixB)






# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

# https://docs.python.org/3/reference/expressions.html#calls

#https://www.programiz.com/python-programming/list-comprehension