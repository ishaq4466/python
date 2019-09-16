

avengers = [["Spidy","Ironman","Hulk", "Falcon", "Vision"],[28, 53, 48, 35, 5],["M", "M","M","M", "N/A"]]

dict = {"Name":avengers[0], "Age":avengers[1], "Gender":avengers[2]}

i = 0

print("Avengers Basic Details\n=======================================================")
while i < len(avengers[0]) :
 print("Name:" + str(avengers[0][i]) + "\nAge: " + str(avengers[1][i]) + "\nGender: "+ str(avengers[2][i]))
 print("")
 i=i+1



#Printing it from the dictionary
for t in dict["Name"], dict["Age"]:
 print(t)
