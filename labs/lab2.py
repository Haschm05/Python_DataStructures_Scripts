from ast import If
from symtable import Class
from hashlib import new


def get_valid_severity():
	ids = []
	callers = []
	emergency_types = []
	peoples = []
	priorities = []
	distances = []
	
	num_calls = input("How many calls are you reporting? ")
	while not num_calls.isdigit() or int(num_calls) <= 0:
		print("Please input a valid number ")
		num_calls = input("How many calls are you reporting? ")
	
	for I in range(int(num_calls)):
		call_id = 1 + I
		caller_name = input("What is the callers name? ")
		emergency_type_num = input("What type of emergency do you have? press 1 for medical, " \
                                    "2 for fire, 3 for traffic, 4 for police, 5 for other ")
		while not emergency_type_num.isdigit() or int(emergency_type_num) < 1 or int(emergency_type_num) > 5:
			print("Please input a number between 1 and 5")
			emergency_type_num = input("What type of emergency do you have? press 1 for medical, " \
                                        "2 for fire, 3 for traffic, 4 for police, 5 for other ")
		
		num_people = input("How many people are effected by your emergency? ")
		while not num_people.isdigit() or int(num_people) <= 0:
			print("Please input a valid number ")
			num_people = input("How many people are effected by your emergency? ")
		num_people = int(num_people)
			
		temp_val = input("Are there people in immediate danger? ")
		while not (temp_val == "yes" or temp_val == "no"):
			print("Please enter yes or no ")
			temp_val = input("Are there people in immediate danger? ")
			
		dist = input("How close are you to an emergency responder/response center (in miles)? ")
		while not float(dist) >= 0:
			print("Please input a valid number")
			dist = input("How close are you to an emergency responder/response center? ")
			dist = float(dist)
		
		if emergency_type_num == "1":
			emergency_type = "Medical"
		elif emergency_type_num == "2":
			emergency_type = "Fire"
		elif emergency_type_num == "3":
			emergency_type = "Traffic"
		elif emergency_type_num == "4":
			emergency_type = "Police"
		else:
			emergency_type = "other"
		
		if temp_val == "yes":
			danger = True
		elif temp_val == "no":
			danger = False
			
		ids.append(call_id)
		callers.append(caller_name)
		peoples.append(num_people)
		emergency_types.append(emergency_type)
		priorities.append(danger)
		distances.append(dist)

		print("Call ID: ", call_id)
		print("Caller Name: ", caller_name)
		print("Emergency Type: ", emergency_type)
		print("Number of People Affected: ", num_people)
		print("Immediate Danger: ", danger)
		print("Distance to Emergency Responder: ", dist, "miles")
	
	return ids, callers, peoples, emergency_types, priorities, distances
		
		


def calculate_people_points(peoples):
	scores = []
	score = 0
	
	for I in range(len(peoples)):
		num_people = peoples[I]
		
		if num_people == 1:
			score += 2
		elif num_people <= 3:
			score += 5
		elif num_people <=10:
			score += 10
		else: 
			score += 15
		
		scores.append(score)
		print("Score: ",score)

	return scores


def calculate_type_points(emergency_types, scores):
	
	for I in range(len(scores)):
		type = emergency_types[I]
		score = scores[I]
		
		if type == "Fire":
			score += 10
		elif type == "Medical":
			score += 8
		elif type == "Police":
			score += 6
		elif type == "Traffic":
			score += 4
		else:
			score += 2
			
		scores[I] = score
		print("Score: ",score)
	
	return scores


def calculate_distance_points(distances, scores):
	
	for I in range(len(distances)):
		dist = distances[I]
		score = scores[I]

		dist = float(dist)
		
		if dist > 0 and dist <= 5:
			score += 5
		elif dist > 5 and dist <= 15:
			score += 3
		else:
			score += 1
		
		scores[I] = score
		print("Score: ",score)
	
	return scores


def calculate_priority_score(priorities, scores):
	
	for I in range(len(priorities)):
		priority = priorities[I]
		score = scores[I]
		
		if priority == True:
			score += 25
	
		scores[I] = score
		print("Score: ",score)
		
	return scores


def classify_emergency(scores):
	classes = []
	
	for I in range(len(scores)):
		score = scores[I]
		
		if score >= 80:
			classification = "CRITICAL"
		elif score >= 60:
			classification = "HIGH"
		elif score >= 40:
			classification = "MODERATE"
		else:
			classification = "LOW"

		classes.append(classification)
		print(classification, "Emergency Classification")
	
	return classes

"""
display_emergency()
"""

def main():
    ids, callers, peoples, emergency_types, priorities, distances = get_valid_severity()
    scores = calculate_people_points(peoples)
    scores = calculate_type_points(emergency_types, scores)
    scores = calculate_distance_points(distances, scores)
    scores = calculate_priority_score(priorities, scores)
    classes = classify_emergency(scores)
    #display_emergency(ids, callers, peoples, emergency_types, priorities, distances, scores, classes)

if __name__ == "__main__":
    main()

	
