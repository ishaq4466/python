# import requests
# from bs4 import BeautifulSoup

# j=0
# i=0
# while j<1:
# 	print("j= "+str(j))
# 	print("i= "+str(i))
# 	b_url ="https://www.yelp.com/search?find_loc="
# 	loc="London"
# 	url= b_url +loc+"&start=%s&cflt=restaurants"%(str(j))
# 	file="Hotel-{name}.txt".format(name=loc)

# 	req = requests.get(url)
# 	print(req.status_code)
# 	html_parser = BeautifulSoup(req.text,"html.parser")
# 	largebusinss = html_parser.findAll("div",{"class":"biz-listing-large"})

# 	with open(file,"a") as text:
# 		for t in largebusinss:
# 			try:
# 				title = t.find("a",{"class":"biz-name"}).text
# 				print(title)
# 			except:
# 				title = None
# 			try:
# 					addr = t.find("address").text
# 					print(addr)
# 			except:
# 					addr = None
# 			try:
# 					phone = t.find("span",{"class":"biz-phone"}).text
# 					print(phone)
# 			except:
# 					phone = None

# 			content="({3})Hotel name:{0}\nAddress:{1}\nPhone:{2}\n".format(title,addr.strip(
# 	        ),phone.lstrip(
# 	            ),str(i+1))
# 			text.write(content)

# 			i+=1
# 	j = j+30
# text.close()
# '''sdafaddffdfdsf'''

str1 = "    sdfmsfkkff\n\t\tsdfdsfdslfsdfkdfdf\n   fkdlfdl      "
print(str1.strip("    \n\t\t\n   "))












