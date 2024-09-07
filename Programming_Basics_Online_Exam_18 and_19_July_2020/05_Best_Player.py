command = input()

best_player = ""
most_goals = 0
while command != "END":
    player = command
    goals_scored = int(input())
    if goals_scored >= 10:
        best_player = player
        most_goals = goals_scored
        break
    if goals_scored > most_goals:
        best_player = player
        most_goals = goals_scored

    command = input()
print(f"{best_player} is the best player!")

if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
