floors = int(input())
rooms = int(input())

floor_letter = ""
for floor in range(floors, 0, -1):
    if floor == floors:
        floor_letter = "L"
    elif floor % 2 == 0:
        floor_letter = "O"
    else:
        floor_letter = "A"
    for room in range(rooms):
        print(f"{floor_letter}{floor}{room}", end=" ")
    print()
