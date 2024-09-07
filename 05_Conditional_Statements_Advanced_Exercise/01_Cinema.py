#My way
# screening_type = input()
# row_number = int(input())
# column_number = int(input())
#
# ticket_price = 0
#
# if screening_type == "Premiere":
#     ticket_price = 12.00
# elif screening_type == "Normal":
#     ticket_price = 7.50
# elif screening_type == "Discount":
#     ticket_price = 5.00
#
# total_cost = ticket_price * row_number * column_number
# print(f"{total_cost :.2f} leva")

screening_type = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns

if screening_type == "Premiere":
    income = cinema_capacity * 12.00
elif screening_type == "Normal":
    income = cinema_capacity * 7.50
elif screening_type == "Discount":
    income = cinema_capacity * 5.00
print(f"{income :.2f} leva")
