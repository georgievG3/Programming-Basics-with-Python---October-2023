count_of_numbers = int(input())

p1_number = 0
p2_number = 0
p3_number = 0
p4_number = 0
p5_number = 0

for _ in range(count_of_numbers):
    numbers = int(input())

    if numbers < 200:
        p1_number += 1
    elif 200 <= numbers <= 399:
        p2_number += 1
    elif 400 <= numbers <= 599:
        p3_number += 1
    elif 600 <= numbers <= 799:
        p4_number += 1
    elif numbers >= 800:
        p5_number += 1

p1_percent = p1_number / count_of_numbers * 100
p2_percent = p2_number / count_of_numbers * 100
p3_percent = p3_number / count_of_numbers * 100
p4_percent = p4_number / count_of_numbers * 100
p5_percent = p5_number / count_of_numbers * 100

print(f"{p1_percent :.2f}%")
print(f"{p2_percent :.2f}%")
print(f"{p3_percent :.2f}%")
print(f"{p4_percent :.2f}%")
print(f"{p5_percent :.2f}%")
