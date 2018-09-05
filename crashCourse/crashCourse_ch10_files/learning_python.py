filename = 'learning_python.txt'


# 1 ***************************************
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# 2 ***************************************
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


# 3 ***************************************
with open(filename) as file_object:
    lines = file_object.readlines()

py_string = ''
for line in lines:
    py_string += line.rstrip()

print(py_string)

# 10-2 Replace ****************************

with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Line', 'hello').rstrip())
