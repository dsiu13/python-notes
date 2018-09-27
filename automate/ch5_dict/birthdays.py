# Say you wanted your program to store data about your friends’ birthdays.
# You can use a dictionary with the names as keys and the birthdays as values.

# Create inital dictionary to store birthdays
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == ''
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    # Adding if it doesn't exist
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
    # any data entered will be erased when the program terminates
