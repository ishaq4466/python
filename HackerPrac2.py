
# Getting the second runner up problem

def removeDuplicate(arr):
	returnList=[]
	for x in arr:
		if x not in returnList:
			returnList.append(x)
	return returnList

def getRunnerUp(arr):
	# print(arr)
	arr=removeDuplicate(arr)
	# print(arr)
	arr=sorted(arr,reverse=True)
	# print(arr)
	# print(arr[1])
	return arr[1]
	
# arr=[2,3,6,6,5]
# print(getRunnerUp(arr))


# Second highest/lowest marks in exams

def prepare_marksheet():
	return [ [input("student name: "),float(input("student marks: ")) ] for _ in range(int(input("Enter the number of students entries: ")))]

# PassIn: list of list i.e nested list
# 1.fetching all the marks and storing it into a list
# 2.convert that marks list to set
# 3.sorting the set as list 
# 4.fetching the second element which will the second_highest marks
# 5. Sorting the marksheet list for lexicograhy
# 6.looping through the marksheet nested list with name and marks 
# 7.if marks == second_highest
#  	store that name to a second_highest_candidates list
# 8.Return the second_highest_candidates list

def get_second_highest_candidate(arr):
	markslist=[ marks for name, marks in arr ]
	print(markslist)
	markslist=set(markslist)
	print(markslist)
	markslist=sorted(markslist,reverse=False) #sorted(markslist,reverse=True)
	print(markslist)
	second_highest_marks=markslist[1]
	print(second_highest_marks)
	print(arr)
	arr=sorted(arr)
	print(arr)
	second_highest_candidates= [ name for name,marks in arr if marks==second_highest_marks ]
	print(second_highest_candidates)
	return second_highest_candidates

# marksheet=prepare_marksheet() # [['abby',45],['asy',48.5]]
# # print(get_second_highest_candidate(marksheet))
# print('\n'.join(get_second_highest_candidate(marksheet)))


# Problem 3: Get avegerage marks for a student

def get_avg_marks(student_marks,query_name):
	# avg_marks
	for key in student_marks.keys():
		if key==query_name:
			avg_marks=sum(student_marks[key])
			print(avg_marks)
	return avg_marks
student_marks={"A":[45,5.6,85],"C":[45,5.6,85],"D":[4,56.4,85]}
query_name="D"
# get_avg_marks(student_marks,query_name)
















