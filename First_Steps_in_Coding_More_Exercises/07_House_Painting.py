RED_PAINT = 4.3
GREED_PAINT = 3.4

house_height = float(input())
house_length = float(input())
roof_height = float(input())

front_back_wall = (house_height * house_height) * 2 - 2.4
side_walls = (house_height * house_length) * 2 - 4.5
roof_tops = (house_height * house_length) * 2
roof_sides = 2 * (house_height * roof_height / 2)

needed_green_paint = (front_back_wall + side_walls) / GREED_PAINT
needed_red_paint = (roof_tops + roof_sides) / RED_PAINT

print(f"{needed_green_paint:.2f}")
print(f"{needed_red_paint:.2f}")
