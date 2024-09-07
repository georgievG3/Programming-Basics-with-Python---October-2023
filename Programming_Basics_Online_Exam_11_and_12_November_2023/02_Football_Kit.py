shirt_price = float(input())
needed_sum = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = 2 * (shirt_price + shorts_price)

total_sum = shirt_price + shoes_price + shorts_price + socks_price
final_sum = total_sum * (1 - 0.15)

if final_sum >= needed_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {final_sum:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_sum - final_sum:.2f} lv. more.")
