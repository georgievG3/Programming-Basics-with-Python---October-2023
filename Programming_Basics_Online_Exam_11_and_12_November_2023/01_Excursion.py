NIGHT_STAY_PRICE = 20
TRANSPORT_CARD_PRICE = 1.60
MUSEUM_TICKET_PRICE = 6

group_people_count = int(input())
nights_count = int(input())
transport_card_count = int(input())
museum_tickets_count = int(input())

nights_price = nights_count * NIGHT_STAY_PRICE
transport_card_price = transport_card_count * TRANSPORT_CARD_PRICE
museum_ticket_price = museum_tickets_count * MUSEUM_TICKET_PRICE

one_person_total = nights_price + transport_card_price + museum_ticket_price
group_total = one_person_total * group_people_count

final_cost = group_total * (1 + 0.25)

print(f"{final_cost:.2f}")
