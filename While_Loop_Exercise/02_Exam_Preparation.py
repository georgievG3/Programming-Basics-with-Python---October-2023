bad_grades = int(input())

bad_grades_count = 0
grades_total = 0
number_of_problems = 0
last_problem = ""

bad_grades_reached = False
command = input()
while command != "Enough":
    problem_name = command
    grade = int(input())
    grades_total += grade
    last_problem = problem_name
    if grade <= 4:
        bad_grades_count += 1
    if bad_grades_count >= bad_grades:
        bad_grades_reached = True
        break
    number_of_problems += 1
    command = input()

average_score = grades_total / number_of_problems

if bad_grades_reached:
    print(f"You need a break, {bad_grades_count} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
