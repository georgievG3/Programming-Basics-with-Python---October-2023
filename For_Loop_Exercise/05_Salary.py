open_tabs = int(input())
salary = int(input())

for open_website in range(open_tabs):
    website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(salary)
