bread = int(input())

winner_points = 0
winner_baker = ""
for _ in range(bread):
    points = 0
    baker_name = input()  #or baker name
    command = int(input())
    while command != "Stop":
        points += int(command)

        command = input()

    print(f"{baker_name} has {points} points.")

    if points > winner_points:
        winner_baker = baker_name
        winner_points = points

        print(f"{baker_name} is the new number 1!")

print(f"{winner_baker} won competition with {winner_points} points!")
