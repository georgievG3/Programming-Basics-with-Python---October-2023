pc_count = int(input())

sales = 0
total_rating = 0
for n in range(pc_count):
    number = int(input())
    rating = number % 10
    total_rating += rating
    possible_sales = number // 10
    if rating == 2:
        sales += 0
    elif rating == 3:
        sales += possible_sales * 0.50
    elif rating == 4:
        sales += possible_sales * 0.70
    elif rating == 5:
        sales += possible_sales * 0.85
    elif rating == 6:
        sales += possible_sales

print(f"{sales:.2f}")
print(f"{total_rating / pc_count:.2f}")
