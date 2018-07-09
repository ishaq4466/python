# Dictionary can be use in CMSys in flask

list1 = [ ["Index page","/index/"], ["Login page","/login/"], ["Signup","/signup/"]]
TOPIC_DICT={"Homepage":list1, "FirstPage":"list2"}

for t in TOPIC_DICT["Homepage"]:
 print(t[0])

for t in TOPIC_DICT["Homepage"]:
 print(t[1])



