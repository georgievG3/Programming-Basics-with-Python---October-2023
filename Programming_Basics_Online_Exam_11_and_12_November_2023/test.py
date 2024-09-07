sea_count = int(input())
mountain_count = int(input())

revenue = 0
command = input()
is_sold = False
while command != "Stop":
    packet = command
    if packet == "sea" and sea_count <= 0:
        command = input()
        continue
    elif packet == "mountain" and mountain_count <= 0:
        command = input()
        continue
    elif packet == "sea":
        revenue += 680
        sea_count -= 1
    elif packet == "mountain":
        revenue += 499
        mountain_count -= 1

    if sea_count <= 0 and mountain_count <= 0:
        is_sold = True
        break

    command = input()
if is_sold:
    print("Good job! Everything is sold.")
print(f"Profit: {revenue} leva.")