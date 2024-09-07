start = int(input())
stop = int(input())
magic_number = int(input())

counter = 0
equal = False
for first_number in range(start, stop + 1):
    for second_number in range(start, stop + 1):
        counter += 1
        result = first_number + second_number
        if result == magic_number:
            equal = True
            break
    if equal:
        break
if equal:
    print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")
