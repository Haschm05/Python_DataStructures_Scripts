from ast import If
from symtable import Class

#Get valid score takes inputs from the user and validates that the inputs are within the parameters
def get_valid_score():
    student_names = []
    exam_scores = []
    project_scores = []
    lab_scores = []
    comp_assigns = []
    tot_assigns = []

    loop = input("how many students would you like to enter? ")
    if not loop.isdigit():
        while not loop.isdigit() or int(loop) <= 0 or int(loop) > 20:
            print("Please enter a valid number.")
            loop = input("how many students would you like to enter? ")

    for I in range(int(loop)):
        student_name = str(input("Enter students' name: "))
        exam_score = input("Enter exam score: ")

        if not exam_score.isdigit():
            while not exam_score.isdigit():
                print("Please enter a valid score between 0 and 100.")
                exam_score = input("Enter exam score: ")
                project_score = input("Enter project score: ")

        if not project_score.isdigit():
            while not project_score.isdigit():
                print("Please enter a valid score between 0 and 100.")
                project_score = input("Enter project score: ")
                lab_score = input("Enter lab score: ")

        if not lab_score.isdigit():
            while not lab_score.isdigit():
                print("Please enter a valid score between 0 and 100.")
                lab_score = input("Enter lab score: ")
                completed_assignments = input("Enter number of assignments completed: ")

        if not completed_assignments.isdigit():
            while not completed_assignments.isdigit():
                print("Please enter a valid number.")
                completed_assignments = input("Enter number of assignments completed: ")
                total_assignments = input("Enter total number of assignments: ")

        if not total_assignments.isdigit():
            while not total_assignments.isdigit():
                print("Please enter a valid number.")
                total_assignments = input("Enter total number of assignments: ")

        exam_score = float(exam_score)
        project_score = float(project_score)
        lab_score = float(lab_score)
        completed_assignments = int(completed_assignments)
        total_assignments = (total_assignments)
        student_names.append(student_name)
        exam_scores.append(exam_score)
        project_scores.append(project_score)
        lab_scores.append(lab_score)
        comp_assigns.append(completed_assignments)
        tot_assigns.append(total_assignments)

    return student_names, exam_scores, project_scores, lab_scores, comp_assigns, tot_assigns


def calculate_weighted_average(exam_scores, project_scores, lab_scores):
    weighted_avgs = []

    for i in range(len(exam_scores)):
        exam_score = exam_scores[i]
        project_score = project_scores[i]
        lab_score = lab_scores[i]
        score = (exam_score * .4) + (project_score * .35) + (lab_score * .25)
        weighted_avgs.append(score)

    return weighted_avgs


def calculate_completion_percentage(comp_assigns, tot_assigs):
    completion_percentages = []

    for i in range(len(comp_assigns)):
        completed_assignments = comp_assigns[i]
        total_assignments = tot_assigs[i]
        total_assignments = int(total_assignments)
        completed_assignments = int(completed_assignments)

        if total_assignments > 0:
            percentage = (completed_assignments / total_assignments) * 100
        else:
            percentage = 0
        completion_percentages.append(percentage)

    return completion_percentages


def determine_letter_grade(weighted_avgs):
    letter_grades = []

    for i in range(len(weighted_avgs)):
        score = weighted_avgs[i]
        if score >= 90:
            letter_grade = "A"
        elif score >= 80:
            letter_grade = "B"
        elif score >= 70:
            letter_grade = "C"
        elif score >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"

        letter_grades.append(letter_grade)
    return letter_grades


def determine_status(weighted_avgs, completion_percentages):
    statuses = []

    for i in range(len(weighted_avgs)):
        weighted_avg = weighted_avgs[i]
        completion_percentage = completion_percentages[i]

        if weighted_avg >= 90 and completion_percentage >= 90:
            status = "Excellent Standing"
        elif weighted_avg >= 75 and completion_percentage >= 80:
            status = "Good Standing"
        elif weighted_avg >= 60 or completion_percentage >= 70:
            status = "Needs Attention"
        else:
            status = "At Risk"
        statuses.append(status)

    return statuses


def display_student_report(student_names, exam_scores, project_scores, lab_scores,
    weighted_avgs, letter_grades, comp_assigns, tot_assigns, completion_percentages, statuses):

    for i in range(len(student_names)):
        student_name = student_names[i]
        exam_score = exam_scores[i]
        project_score = project_scores[i]
        lab_score = lab_scores[i]
        weighted_avg = weighted_avgs[i]
        letter_grade = letter_grades[i]
        completed_assignments = comp_assigns[i]
        total_assignments = tot_assigns[i]
        completion_percentage = completion_percentages[i]
        status = statuses[i]
        print("Student Performance Report")
        print("--------------------------------")
        print(f"Student: {student_name}")
        print(f"Exam: {exam_score:.2f}")
        print(f"Project: {project_score:.2f}")
        print(f"Lab: {lab_score:.2f}")
        print(f"Weighted Average: {weighted_avg:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"Assignments Completed: {completed_assignments} of {total_assignments}")
        print(f"Completion Percentage: {completion_percentage:.2f}%")
        print(f"Status: {status}")
        print()


def display_class_summary(student_names, weighted_avgs, letter_grades):
    # This function will calculate and display the class summary requirements
    number_of_students = len(student_names)
    class_average = sum(weighted_avgs) / number_of_students
    highest_student_average = max(weighted_avgs)
    lowest_student_average = min(weighted_avgs)
    number_of_A_grades = letter_grades.count("A")
    number_of_B_grades = letter_grades.count("B")
    number_of_C_grades = letter_grades.count("C")
    number_of_D_grades = letter_grades.count("D")
    number_of_F_grades = letter_grades.count("F")
    print("Class Summary")
    print("---------------------")
    print(f"Number of Students: {number_of_students}")
    print(f"Class Average: {class_average:.2f}")
    print(f"Highest Student Average: {highest_student_average:.2f}")
    print(f"Lowest Student Average: {lowest_student_average:.2f}")
    print(f"Number of A Grades: {number_of_A_grades}")
    print(f"Number of B Grades: {number_of_B_grades}")
    print(f"Number of C Grades: {number_of_C_grades}")
    print(f"Number of D Grades: {number_of_D_grades}")
    print(f"Number of F Grades: {number_of_F_grades}")


def main():
    student_names, exam_scores, project_scores, lab_scores, comp_assigns, tot_assigns = get_valid_score()

    letter_grades = calculate_weighted_average(exam_scores, project_scores, lab_scores)

    completion_percentages = calculate_completion_percentage(comp_assigns, tot_assigns)

    weighted_avgs = calculate_weighted_average(exam_scores, project_scores, lab_scores)

    letter_grades = determine_letter_grade(weighted_avgs)

    statuses = determine_status(weighted_avgs, completion_percentages)

    display_student_report(student_names, exam_scores, project_scores, lab_scores, weighted_avgs, letter_grades,
                           comp_assigns, tot_assigns, completion_percentages, statuses)

    display_class_summary(student_names, weighted_avgs, letter_grades)


if __name__ == "__main__":
    main()