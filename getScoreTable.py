def get_first_table(players):
	print(players)
	players_score=set([ score for name,score in players ])
	print(players_score)

def get_score_table(players):
	# print(players)
	scores_list=list(set([ score for name,score in players]))
	# print(scores_list)
	sorted_score=sorted(scores_list,reverse=True)
	# print(sorted_score)
	returnArr=[]
	for x in sorted_score:
		for a,b in players:
			if x==b:
				returnArr.append([a,b])
	return returnArr
	# score_list=[]
	# for score in sorted_score:


	# print(scores_list)


name=["rohit","virat","ajinkya","kedar","abhi","dhoni"]
score=[12,74,11,74,85,0]

players=[ [name[x],score[x]] for x in range(len(name)) ]
# for x in range(len(name)):
	# players.append([name[x],score[x]])
print("Calling the get_score_table function for ordering in desc")
for x in get_score_table(players):
	print(x)

