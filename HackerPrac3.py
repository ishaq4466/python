

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


tup1=(1,2,3,"ahas","22")
print(tup1)
tup1.add(1)
# tup1=list(tup1)
tup1[0]='33'
