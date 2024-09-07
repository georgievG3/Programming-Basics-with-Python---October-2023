LITRE_FUEL_PRICE = 2.10
TOUR_GUIDE_PRICE = 100

budget = float(input())
litre_fuel_needed = float(input())
day_of_the_week = input()

fuel_cost = litre_fuel_needed * LITRE_FUEL_PRICE
fuel_cost_with_tour = fuel_cost + TOUR_GUIDE_PRICE

total_cost = 0

if day_of_the_week == "Sunday":
    total_cost = fuel_cost_with_tour - (fuel_cost_with_tour * 0.20)
elif day_of_the_week == "Saturday":
    total_cost = fuel_cost_with_tour - (fuel_cost_with_tour * 0.10)

money_left = budget - total_cost

if total_cost <= budget:
    print(f"Safari time! Money left: {money_left:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {-money_left:.2f} lv.")
