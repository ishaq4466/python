
# [ expression for items in list ]
arr1=[ x for x in range(0,11) ]

print(arr1)

print([ [i,j] for i in range(0,3) for j in range(0,3) ] )

print([ [i,j]	 if i==j else [0,0,0]  for i in range(0,3) for j in range(0,3) if i==j ] )




# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

# https://docs.python.org/3/reference/expressions.html#calls

#https://www.programiz.com/python-programming/list-comprehension