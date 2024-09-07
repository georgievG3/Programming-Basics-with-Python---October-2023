budget = int(input())
season = input()
fisherman_count = int(input())

rent_price = 0
discount = 0

if season == "Spring":
    rent_price = 3000
elif season == "Summer" or season == "Autumn":
    rent_price = 4200
elif season == "Winter":
    rent_price = 2600

if fisherman_count <= 6:
    discount = 0.10
elif 7 <= fisherman_count <= 11:
    discount = 0.15
elif fisherman_count >= 12:
    discount = 0.25

total_cost = rent_price * (1 - discount)

if fisherman_count % 2 == 0 and season != "Autumn":
    total_cost *= 0.95

if budget >= total_cost:
    print(f"Yes! You have {budget - total_cost :.2f} leva left.")
else:
    print(f"Not enough money! You need {total_cost - budget :.2f} leva.")
