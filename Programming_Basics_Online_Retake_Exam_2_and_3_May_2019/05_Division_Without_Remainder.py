numbers = int(input())

two_counter = 0
three_counter = 0
four_counter = 0
for _ in range(numbers):
    number = int(input())
    if number % 2 == 0:
        two_counter += 1
    if number % 3 == 0:
        three_counter += 1
    if number % 4 == 0:
        four_counter += 1

p1 = two_counter / numbers * 100
p2 = three_counter / numbers * 100
p3 = four_counter / numbers * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
