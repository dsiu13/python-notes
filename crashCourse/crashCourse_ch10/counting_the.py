#10-10 Common Words - Count the number of 'the' that appear

filename = "alice_wonderland.txt"

def reading():
    with open(filename) as f_obj:
        lines = f_obj.readlines()

    for line in lines:
        line.lower().count('the')


reading()
