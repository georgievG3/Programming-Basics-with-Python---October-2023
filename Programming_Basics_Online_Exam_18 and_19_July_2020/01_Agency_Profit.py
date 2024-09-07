airline_name = input()
elders_ticket_count = int(input())
kids_ticket_count = int(input())
elders_ticket_price = float(input())
tax = float(input())

final_kids_ticket_price = elders_ticket_price - (elders_ticket_price * 0.70) + tax
final_elder_ticket_price = elders_ticket_price + tax

elders_profit = elders_ticket_count * final_elder_ticket_price
kids_profit = kids_ticket_count * final_kids_ticket_price

total_price = elders_profit + kids_profit
total_profit = total_price * 0.20

print(f"The profit of your agency from {airline_name} tickets is {total_profit:.2f} lv.")
