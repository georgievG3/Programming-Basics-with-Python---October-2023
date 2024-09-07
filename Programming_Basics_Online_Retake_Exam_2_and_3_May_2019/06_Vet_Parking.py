day_count = int(input())
hours_per_day = int(input())

total_cost = 0

for day in range(1, day_count + 1):
    day_total_cost = 0

    for hours in range(1, hours_per_day + 1):
        if day % 2 == 0 and hours % 2 != 0:
            day_total_cost += 2.50
        elif day % 2 != 0 and hours % 2 == 0:
            day_total_cost += 1.25
        else:
            day_total_cost += 1

    total_cost += day_total_cost

    print(f"Day: {day} - {day_total_cost:.2f} leva")


print(f"Total: {total_cost:.2f} leva")
