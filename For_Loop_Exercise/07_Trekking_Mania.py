group_count = int(input())

musala_people = 0
monblan_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0

total_people = 0

for _ in range(group_count):
    people_in_group = int(input())
    total_people += people_in_group

    if people_in_group <= 5:
        musala_people += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan_people += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimanjaro_people += people_in_group
    elif 26 <= people_in_group <= 40:
        k2_people += people_in_group
    else:
        everest_people += people_in_group

musala_percent = musala_people / total_people * 100
monblan_percent = monblan_people / total_people * 100
kilimanjaro_percent = kilimanjaro_people / total_people * 100
k2_percent = k2_people / total_people * 100
everest_percent = everest_people / total_people * 100

print(f"{musala_percent :.2f}%")
print(f"{monblan_percent :.2f}%")
print(f"{kilimanjaro_percent :.2f}%")
print(f"{k2_percent :.2f}%")
print(f"{everest_percent :.2f}%")
