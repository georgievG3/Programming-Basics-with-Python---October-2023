total = 0

deposit = input()
while deposit != "NoMoreMoney":
    money = float(deposit)
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    total += money
    deposit = input()
print(f"Total: {total:.2f}")
