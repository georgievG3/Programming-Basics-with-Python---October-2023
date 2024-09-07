number = int(input())

for special_numbers in range(1111, 10000):
    is_special = True
    special_str = str(special_numbers)
    for index, digit in enumerate(special_str):
        current_digit = int(digit)
        if current_digit == 0:
            is_special = False
            break
        if not number % current_digit == 0:
            is_special = False
            break
    if is_special:
        print(f"{special_numbers}", end=" ")
