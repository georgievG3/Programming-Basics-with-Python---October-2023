CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15
DELIVERY = 2.50

amount_chicken_menu = int(input())
amount_fish_menu = int(input())
amount_vegetarian_menu = int(input())

final_chicken_price = amount_chicken_menu * CHICKEN_MENU
final_fish_price = amount_fish_menu * FISH_MENU
final_vegetarian_price = amount_vegetarian_menu * VEGETARIAN_MENU

menu_price = final_chicken_price + final_fish_price + final_vegetarian_price

desert_price = menu_price * 0.20

final_price = menu_price + desert_price + 2.50

print(final_price)
