days_of_tournament = int(input())

total_money = 0
win_counter = 0
lose_counter = 0
total_win_counter = 0
total_lose_counter = 0
money_won = 0
for days in range(days_of_tournament):
    command = input()
    while command != "Finish":
        win_or_lose = input()
        if win_or_lose == "win":
            money_won += 20
            win_counter += 1
            total_win_counter += 1
        else:
            lose_counter += 1
            total_lose_counter += 1

        command = input()

    if win_counter > lose_counter:
        money_won *= (1 + 0.10)
        total_money += money_won
        money_won = 0
        win_counter = 0
        lose_counter = 0
    else:
        total_money += money_won
        money_won = 0
        win_counter = 0
        lose_counter = 0

if total_win_counter > total_lose_counter:
    total_money *= (1 + 0.20)
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
