# 10-6
def add_numbers():
    try:
        x = int(input("Enter your 1st number: "))
        y = int(input("Enter your 2nd number: "))
    except ValueError:
        print('please enter a number')
        add_numbers()
    else:
        print(x + y)

add_numbers()
