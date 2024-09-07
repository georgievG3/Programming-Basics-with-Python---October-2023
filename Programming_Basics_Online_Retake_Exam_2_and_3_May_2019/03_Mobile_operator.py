ONE_YEAR_SMALL_PRICE = 9.98
ONE_YEAR_MIDDLE_PRICE = 18.99
ONE_YEAR_LARGE_PRICE = 25.98
ONE_YEAR_EXTRA_LARGE_PRICE = 35.99

TWO_YEAR_SMALL_PRICE = 8.58
TWO_YEAR_MIDDLE_PRICE = 17.09
TWO_YEAR_LARGE_PRICE = 23.59
TWO_YEAR_EXTRA_LARGE_PRICE = 31.79

contract_duration = input()
contract_type = input()
internet_added = input()
months_to_pay = int(input())

contract_price = 0

if contract_duration == "one" and contract_type == "Small":
    contract_price += ONE_YEAR_SMALL_PRICE
elif contract_duration == "one" and contract_type == "Middle":
    contract_price += ONE_YEAR_MIDDLE_PRICE
elif contract_duration == "one" and contract_type == "Large":
    contract_price += ONE_YEAR_LARGE_PRICE
elif contract_duration == "one" and contract_type == "ExtraLarge":
    contract_price += ONE_YEAR_EXTRA_LARGE_PRICE
elif contract_duration == "two" and contract_type == "Small":
    contract_price += TWO_YEAR_SMALL_PRICE
elif contract_duration == "two" and contract_type == "Middle":
    contract_price += TWO_YEAR_MIDDLE_PRICE
elif contract_duration == "two" and contract_type == "Large":
    contract_price += TWO_YEAR_LARGE_PRICE
elif contract_duration == "two" and contract_type == "ExtraLarge":
    contract_price += TWO_YEAR_EXTRA_LARGE_PRICE

if internet_added == "yes" and contract_price <= 10:
    contract_price += 5.50
elif internet_added == "yes" and 10 < contract_price <= 30:
    contract_price += 4.35
elif internet_added == "yes" and contract_price > 30:
    contract_price += 3.85

if contract_duration == "two":
    contract_price *= (1 - 0.0375)
else:
    pass

total_price = contract_price * months_to_pay

print(f"{total_price:.2f} lv.")
