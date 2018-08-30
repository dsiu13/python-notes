file_cats = "cats.txt"
file_dogs = "dogs.txt"

def read_dogs():
    with open(file_dogs) as f_obj:
        lines = f_obj.readlines()

    for line in lines:
        print(line.rstrip() + "\n")

def read_cats():
    with open(file_cats) as f_obj:
        lines = f_obj.readlines()

    for line in lines:
        print(line.rstrip() + "\n")

def cats_dogs():
    try:
        read_dogs()
        read_cats()
    except FileNotFoundError:
        # print('404')
        pass

cats_dogs()
