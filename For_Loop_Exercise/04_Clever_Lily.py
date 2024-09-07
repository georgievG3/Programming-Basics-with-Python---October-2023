lily_age = int(input())
machine_price = float(input())
toy_price = int(input())

money = 0
toys = 0

for year in range(1, lily_age + 1):
    if year % 2 == 0:
        money += year * 5
        money -= 1
    else:
        toys += 1

money_from_toys = toys * toy_price
total_money = money + money_from_toys

if total_money >= machine_price:
    print(f"Yes! {total_money - machine_price :.2f}")
else:
    print(f"No! {machine_price - total_money :.2f}")
