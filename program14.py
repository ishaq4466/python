# File handing using os lib
#Method:os.path.join(), os.getcwd(), os.path.isfile(), open().read()

#opening a text file
import os
path2file_ ="module/template.txt"
#Validating the file existance and path
def get_path(path):
	fpath=os.path.join(os.getcwd(),path)
	if not os.path.isfile(fpath):
		raise Exception("Invalid file path")
	return fpath


# getting the text and reading it
def get_txt(path):
	fpath = get_path(path)
	file = open(fpath).read()
	return file

print(get_txt(path2file_))

# #========================Making the code shorter==================
# #Validating the file existance and path
# def get_path(path):
# 	if not os.path.isfile(os.path.join(os.getcwd(),path)):
# 		raise Exception("Invalid file path")
# 	return os.path.join(os.getcwd(),path)

# # getting the text and reading it

# def get_txt(path):
# 	#file = open(get_path(path)).read()
# 	return open(get_path(path)).read()


# print(get_txt(path2file_))




