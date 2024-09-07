jury = int(input())

total_grade = 0
counter = 0
command = input()
while command != "Finish":
    grade_sum = 0
    for grades in range(jury):
        grade = float(input())
        grade_sum += grade

    average_grade = grade_sum / jury
    print(f"{command} - {average_grade:.2f}.")
    total_grade += average_grade
    counter += 1
    command = input()

total_average = total_grade / counter
print(f"Student's final assessment is {total_average:.2f}.")
