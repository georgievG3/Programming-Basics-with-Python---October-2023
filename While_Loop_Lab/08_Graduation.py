student_name = input()
current_class = 1
total_grade = 0
failed = 0
is_excluded = False

while current_class <= 12:
    year_grade = float(input())
    if year_grade < 4:
        failed += 1
        if failed > 1:
            is_excluded = True
            break
        continue
    current_class += 1
    total_grade += year_grade

if is_excluded:
    print(f"{student_name} has been excluded at {current_class} grade")
else:  # elif is_excluded == False
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
