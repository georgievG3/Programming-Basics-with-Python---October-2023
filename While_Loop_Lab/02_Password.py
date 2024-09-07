username = input()
password = input()

password_attempt = input()
while password_attempt != password:
    password_attempt = input()
print(f"Welcome {username}!")
