number = int(input())

first_digit = number // 100
middle_digit = number // 10 % 10
last_digit = number % 10

for first_multiplier in range(1, last_digit + 1):
    for second_multiplier in range(1, middle_digit + 1):
        for third_multiplier in range(1, first_digit + 1):
            result = first_multiplier * second_multiplier * third_multiplier
            print(f"{first_multiplier} * {second_multiplier} * {third_multiplier} = {result};")
