length = int(input())
width = int(input())

total_pieces = length * width

command = input()
while command != "STOP":
    piece = int(command)
    total_pieces -= piece
    if total_pieces <= 0:
        break
    command = input()
if command == "STOP":
    print(f"{total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {-total_pieces} pieces more.")
