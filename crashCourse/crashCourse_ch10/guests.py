filename = 'guest_book.txt'

# 10-3 Guests
# name = input('enter your name: ')
# with open(filename, 'w') as file_object:
#     file_object.write(name)

# 10-4 Guests
prompt = "Whats you name? "
prompt += "type 'quit' to exit anytime "

msg = ""

while msg != 'quit':
  msg = input(prompt)
  print(msg)
  with open(filename, 'a') as file_object:
      file_object.write(msg + "\n")
  
