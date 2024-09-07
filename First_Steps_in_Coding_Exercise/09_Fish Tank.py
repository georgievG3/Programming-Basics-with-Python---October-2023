length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

fish_tank_volume = length * width * height
fish_tank_volume_in_litres = fish_tank_volume / 1000

water_needed_litres = fish_tank_volume_in_litres * (1 - percentage)

print(water_needed_litres)
