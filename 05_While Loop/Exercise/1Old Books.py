book_found = False
favourite_book = input()
current_book = 0
number = 0

while current_book != favourite_book:
    current_book = input()
    if current_book == 'No More Books':
        book_found = False
        break
    if current_book == favourite_book:
        book_found = True
        break
    else:
        number += 1

if book_found:
    print(f'You checked {number} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {number} books.')
