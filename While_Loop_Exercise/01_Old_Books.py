searched_book = input()
book_count = 0

is_book_found = False
guess_book = input()
while guess_book != searched_book:
    guess_book = input()
    book_count += 1
    if guess_book == "No More Books":
        is_book_found = True
        break
if is_book_found:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
else:
    print(f"You checked {book_count} books and found it.")
