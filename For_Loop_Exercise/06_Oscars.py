actor = input()
academia_points = float(input())
number_of_jury = int(input())

total_points = academia_points

for _ in range(number_of_jury):
    name_of_jury = input()
    points_of_jury = float(input())

    total_points += len(name_of_jury) * points_of_jury / 2

    if total_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points :.1f}!")
        break
else:
    print(f"Sorry, {actor} you need {1250.5 - total_points :.1f} more!")
