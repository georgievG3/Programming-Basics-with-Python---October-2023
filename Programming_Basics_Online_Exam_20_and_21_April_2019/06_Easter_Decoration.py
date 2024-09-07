prices = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7.00,
}

clients = int(input())

total_price = 0

for shop in range(clients):
    items_count = 0
    price_per_client = 0
    command = input()
    while command != "Finish":
        purchase = command
        price = prices[purchase]
        price_per_client += price
        items_count += 1
        command = input()
    if items_count % 2 == 0:
        price_per_client *= (1 - 0.20)

    total_price += price_per_client

    print(f"You purchased {items_count} items for {price_per_client:.2f} leva.")

average_price = total_price / clients

print(f"Average bill per client is: {average_price:.2f} leva.")


