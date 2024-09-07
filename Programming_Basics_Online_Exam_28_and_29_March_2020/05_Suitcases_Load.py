capacity = float(input())

free_capacity = capacity
suitcase_count = 0
all_space_used = False

command = input()
while command != "End":
    suitcase_volume = float(command)
    suitcase_count += 1

    if suitcase_count % 3 == 0:
        suitcase_volume *= (1 + 0.10)

    free_capacity -= suitcase_volume
    if free_capacity < 0:
        suitcase_count -= 1
        all_space_used = True
        break

    command = input()

if all_space_used:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcase_count} suitcases loaded.")

