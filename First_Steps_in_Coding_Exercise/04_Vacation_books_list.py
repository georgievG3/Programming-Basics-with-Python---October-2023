# 1. Брой страници в текущата книга – цяло число в интервала [1…1000]
#
# 2. Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#
# 3. Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours_needed = total_pages // pages_per_hour

hours_per_day_needed = total_hours_needed // days

print(hours_per_day_needed)
