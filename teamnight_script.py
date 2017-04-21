import pandas as pd 
import numpy as np 


participants = []

def add_user():
	print("What is your slack handle?")
	handle = input("@")
	print("About how many lines of Python have you written? ")
	their_linecount = input(">")
	# if type(their_linecount) != int():
	while True:
		try:
			linecount = int(their_linecount) 
			break
		except: 
			print("Please enter an integer.")
			their_linecount = input(">")
	participants.append((handle, linecount))
	print('Thanks! Enjoy project night!')

def get_users():
	while True:
		print("Would you like to join our team project night? Please answer y/n.")
		answer = input(">")
		if answer.lower() == "y":
			add_user()
		else:
			if len(participants) < 4:
				print('too bad, more participants needed')
				pass
			else:
				break


#get_users()

participants = [('nolan', 100000000), ('mike', 10000000), ('amanda', 200)] * 3


participants = sorted(participants, key=lambda x: x[1])
odd_ones = len(participants) % 4
if odd_ones:
	odds = participants[-odd_ones:]
	participants = participants[:-odd_ones]
else:
	odds = None


num_participants = int(len(participants) / 2)
bottom = participants[:num_participants]
top = reversed(participants[num_participants:])

pairs = [pair for pair in zip(bottom, top)]

groups = []

while pairs:
	(user1, user2), (user3, user4) = pairs[:2]
	groups.append([user1[0], user2[0], user3[0], user4[0]])
	pairs = pairs[2:]

for i, person in enumerate(odds):
	groups[i].append(person[0])


for group in groups:
	print(group)








# np.median

# final_list.pop(random_integer)