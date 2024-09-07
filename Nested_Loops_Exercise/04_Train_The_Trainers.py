judges = int(input())
command = input()

all_total_score = 0
total_grade = 0
counter = 0
while command != "Finish":
    for _ in range(judges):
        grade = float(input())
        total_grade += grade
    counter += 1
    avg_grade = total_grade / judges
    all_total_score += avg_grade
    print(f"{command} - {avg_grade:.2f}.")
    total_grade = 0

    command = input()

all_avg_score = all_total_score / counter
print(f"Student's final assessment is {all_avg_score:.2f}.")
