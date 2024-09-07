change = float(input())

coins = 0
change_in_penny = int(change * 100)

while change_in_penny > 0:
    coins += 1
    if change_in_penny >= 200:
        change_in_penny -= 200
    elif change_in_penny >= 100:
        change_in_penny -= 100
    elif change_in_penny >= 50:
        change_in_penny -= 50
    elif change_in_penny >= 20:
        change_in_penny -= 20
    elif change_in_penny >= 10:
        change_in_penny -= 10
    elif change_in_penny >= 5:
        change_in_penny -= 5
    elif change_in_penny >= 2:
        change_in_penny -= 2
    elif change_in_penny >= 1:
        change_in_penny -= 1
print(coins)
