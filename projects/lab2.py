get_valid_severity()
    ids = []
    callers = []
    emergency_types = []
    peoples = []
    priorities = []
    distances = []

    num_calls = input("How many calls are you reporting?")
    if num_calls.isdigit() == False OR num_calls <= 0:
        while num_calls.isdigit() == False:
            num_calls = input("Please enter a positive integer: ")

    for i in range(num_calls):
        Call_id = i
        Caller_name = input("What is the callers name?")

        Emergency_type_num = input("What type of emergency do you have? press 1 for medical,2 "
                                   "for fire, 3 for traffic, 4 for police, 5 for other")
        while Emergency_type_num not = num between 1 and 5:
            print("Please input a number between 1 and 5")
            Emergency_type_num = input("What type of emergency do you have? press 1 for medical, 2"
                                       "for fire, 3 for traffic, 4 for police, 5 for other")

        num_people = input("How many people are effected by your emergency?")
        while num_people not = isdigit() OR num_people not > 0:
            print("Please input a valid number")
            num_people = input("How many people are effected by your emergency?")

        temp_val = input("Are there people in immediate danger?")
        while temp_val not = "yes" or "no":
            print("Please enter yes or no")
            temp_val = input("Are there people in immediate danger?")

        dist = input("How close are you to an emergency responder/response center (in miles)?")
        while dist not = isdigit and > 0:
            print("Please input a valid number")
            dist = input("How close are you to an emergency responder/response center (in miles)?")

        if emergency_type_num = 1:
            emergency_type = "Medical"
        elif emergency_type_num = 2:
            emergency_type = "Fire"
        elif emergency_type_num = 3:
            emergency_type = "Traffic"
        elif emergency_type_num = 4
            emergency_type = "Police"
        else:
            emergency_type = "other"

        if firstdigit(temp_val) = y
            bool danger = True
        elif firstdigit)temp_val = n
            bool danger = False

        ids.append(call_id)
        callers.append(caller_name)
        peoples.append(num_people)
        emergency_types.append(emergency_type)
        priorities.append(bool danger)
        distances.append(dist)

    return ids, callers, peoples, emergency_types, priorities, distances

calculate_people_points(peoples)
    scores = []
    score = 0

    for I in range(len(peoples)
        num_people = peoples[i]

        if num_people = 1:
            score += 2
        elif num_people <= 3:
        score += 5
        elif num_people <= 10:
        score += 10
        else:
        score + 15

        scores.append(score)

    return scores

calculate_type_points(emergency_types, scores)

    for i in range(len(emergency_types))
        type = emergency_types(i)
        score = scores[i]

        if type = "Fire":
            score += 10
        elif type = "Medical":
            score += 8
        elif type = "Police":
            score += 6
        elif type = "Traffic":
            score += 4
        else:
            score += 2

        update scores[i] to new score

    return scores

calculate_distance_points(distances, scores)
    for i in range(len(distances))
        dist = distances[i]
        score = scores[i]

        if dist > 0 AND less than or equal to 5:
            score += 5
        elif dist greater than 5 AND less than 15:
            score += 3
        else:
            score += 1

        update scores[i] to new score

    return scores

calculate_priority_score(priorities, scores)

    for i in range(len(priorities))
        priority = priorities[i]
        score = scores[i]

        if priority = True:
            # Double check these
            priority
            score = severity * 10
            if immediate danger (add 25)

        update scores[i] to new score at i

    return scores

classify_emergency(scores)
    classes = []

    for i in range(len(scores))
        score = scores[i]

        if score >= 80:
            class = "CRITICAL"
        elif score >= 60:
            class = "HIGH"
        elif score >= 40:
            class = "MODERATE"
        else:
            class = "LOW"

        classes.append(class)

    return classes

display_emergency()
