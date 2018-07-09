import re
text_document = open("test.txt","r")
text_str = text_document.read().lower()
# text_str = "Hard work leads to"
frequecy ={}
filter_str = re.findall(r"\b[a-z]{4,15}\b",text_str)
# print(filter_str)
for words in filter_str:
	count =frequecy.get(words,0)
	frequecy[words]=count+1
# print(frequecy)
keys = frequecy.keys()
for key in keys:
	print(key,frequecy[key])

