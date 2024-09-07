hour = int(input())
minute = int(input())

if 0 <= hour <= 23 and 0 <= minute <= 59:
    minute += 15

    if minute >= 60:
        hour += 1
        minute -= 60

    if hour == 24:
        hour = 0

if minute < 10:
    print(f"{hour}:0{minute}")
else:
    print(f"{hour}:{minute}")

