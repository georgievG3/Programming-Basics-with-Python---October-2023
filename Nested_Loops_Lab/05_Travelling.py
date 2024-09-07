destination = input()

while destination != "End":
    budget = float(input())
    total_money = 0
    while total_money < budget:
        money = float(input())
        total_money += money
    else:
        print(f"Going to {destination}!")
    destination = input()
