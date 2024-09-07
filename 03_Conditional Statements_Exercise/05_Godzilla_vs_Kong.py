budget = float(input())
number_extras = int(input())
price_for_clothing = float(input())

film_decor = budget * 0.10
cost_of_clothing = number_extras * price_for_clothing
discount_clothing = 0

if number_extras > 150:
    discount_clothing = cost_of_clothing * 0.10
else:
    discount_clothing = 0

final_clothing_cost = cost_of_clothing - discount_clothing

total_cost = final_clothing_cost + film_decor

if total_cost > budget:
    print(f"Not enough money!\nWingard needs {total_cost - budget :.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {budget - total_cost :.2f} leva left.")


