# File handing with the os library
import os

#file path for the template
filepath = "module/template.txt"

#function for setting the name ...
def setdata(name=None, item=None, amount=None, team=None):
	dicta = {
		"name":name,
		"item":item,
		"amount":amount,
		"team":team
	}
	return dicta

# validating and getting  the full file path
def get_path(path):
	file = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file):
		raise Exception("Invalid file path")
	return file

# opening the template and returning it
def get_template(path):
	filepath = get_path(path)
	template=open(filepath).read()
	return template

# passing the dictionary to the template
def render_template(tem,data):
	rtemplate = tem.format(**data)
	return rtemplate

data = setdata("stark","iron-Fist",900,"titan")
rtemp = get_template(filepath)
print(render_template(rtemp,data))

#=====================Shorting the code===========================
#function for setting the name ...
def setdata(name=None, item=None, amount=None, team=None):
	dicta = {
		"name":name,
		"item":item,
		"amount":amount,
		"team":team
	}
	return dicta

# validating and getting  the full file path
def get_path(path):
	if not os.path.isfile(os.path.join(os.getcwd(), path)):
		raise Exception("Invalid file path")
	return os.path.join(os.getcwd(), path)

# opening the template and returning it
def get_template(path):
	return open(get_path(path)).read()

# passing the dictionary to the template
def render_template(tem,data):
	return tem.format(**data)
print(render_template(get_template(filepath),setdata("stark","iron-Fist",900,"titan")))