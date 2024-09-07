budget = float(input())

command = input()

budget_left = budget
counter = 0
total_price = 0
while command != "Stop":
    product_name = command
    product_price = float(input())
    if product_price > budget:
        break
    counter += 1

    if counter == 3:
        product_price = product_price * 0.50

    total_price += product_price
    budget_left -= product_price

    command = input()

if command == "Stop":
    print(f"You bought {counter} products for {total_price:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {-budget_left:.2f} leva!")
