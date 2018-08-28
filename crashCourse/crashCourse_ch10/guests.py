filename = 'guest_book.txt'

# 10-3 Guests
name = input('enter your name: ')
with open(filename, 'w') as file_object:
    file_object.write(name)

# 10-4 Guests
