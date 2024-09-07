vacation_cost = float(input())
current_money = float(input())

days = 0
days_spending = 0

while current_money < vacation_cost and days_spending < 5:
    action = input()
    money = float(input())
    days += 1
    if action == "save":
        current_money += money
        days_spending = 0
    elif action == "spend":
        current_money -= money
        days_spending += 1
        if current_money < 0:
            current_money = 0
if days_spending == 5:
    print(f"You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")
