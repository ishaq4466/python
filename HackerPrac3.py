import textwrap

def get_operations(n):
	arr=[]
	for _ in range(n):
		s=input().split(" ")
		cmd=s[0]
		# print(s)
		# print(s[1:])
		if cmd!="print":
			print("cmd:{0}".format(cmd))
			print("arr.{0}({1})".format(cmd,",".join(s[1:])))
			eval("arr.{0}({1})".format(cmd,",".join(s[1:])))
			# eval('arr.{0}{1}'.format(cmd,tuple(map(int,arg))))
		else:
			print(arr)

# get_operations(int(input()))


# tup1=(1,2,3,"ahas","22")
# print(tup1)
# tup1.add(1)
# # tup1=list(tup1)
# tup1[0]='33'

# Swap case problem

inputString="HackerRank.com presents \"Pythonist 2.\""

#input().split(" ")
def swap_case(s):
	outputStr=[]
	for x in inputString:
		# print(x)
		if x.islower():
			# print(x.upper())
			outputStr+=x.upper()
		elif x.isupper():
			# print(x.lower())
			outputStr+=x.lower()
		else:
			outputStr+=x
	return ''.join(outputStr)

def split_and_join(line):
		return '-'.join(line.split(" "))
    # write your code here

def mutate_string(string, position, character):
    # print(string,position,character)
    list1=list(string)
    # print(list1)
    list1[position-1]=character
    # print("".join(list1))
    return "".join(list1)

def count_substring(string, sub_string):
		# print("String {0}".format(string))
		# print("subString {0}".format(sub_string))
		# print(string[3*0:3:])
		count=0
		for x in range(len(string)):
				# print(x)
			# print(string.index(x))
			# print(string[x:x+len(sub_string)])
			if string[x:x+len(sub_string)] == sub_string:
				# print("true")
				count+=1
		# print(count)
		return count
def check_for_conditions(string):
    # print(string.isalpha())	
    # print(string)
		print(any(c.isalnum()  for c in string))
		print(any(c.isalpha() for c in string))
		print(any(c.isdigit() for c in string))
		print(any(c.islower() for c in string))
		print(any(c.isupper() for c in string))

def solve(s):
	print(s.split())
	arr=[ x[:1].upper()+x[1:] for x in s.split() ]
	
	for x in s.split():
		print(x[:1].upper()+x[1:])
	print(' '.join([ x[:1].upper()+x[1:] for x in s.split() ]))
	return ' '.join([ x[:1].upper()+x[1:] for x in s.split() ])




print(solve("hello   world  lol"))
# print(inputString.split(" "))

# print(swap_case(inputString)
# print(split_and_join(inputString))

# string=raw_input().strip()
# sub_string = raw_input().strip()
# print(count_substring(string,sub_string))

# print(mutate_string(inputString,3,'z'))

# check_for_conditions("qA2")
# 
# strarr="This is a very very very very very long string."
# strarr="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# print(textwrap.wrap(strarr,4)) # It will retur

# print(textwrap.fill(strarr,4))

# print("Hello".rjust(20,'-'))
# print("Hello".ljust(20,'-'))
# print("Hello".center(20,'-'))

# # Text formatting
# width=len("{0:b}".format(5))
# for x in range(1,12+1):
# 	print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(x,width=width))



