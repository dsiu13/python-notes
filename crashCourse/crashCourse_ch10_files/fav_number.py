import json

# 10-11 Favorite Number
# def fav_number():
#     filename = "fav_number.txt"
#     prompt = input('Enter your favorite number: ')
#     with open(filename, "w") as f_obj:
#       json.dump(prompt, f_obj)
#       print("your fav number is: " + prompt)
#
# fav_number()

def fav_number():
    filename = "fav_number.txt"
    prompt = input('Enter your favorite number: ')
    with open(filename, "w") as f_obj:
      json.dump(prompt, f_obj)

    with open(filename) as file_object:
      fav_num = json.load(file_object)
      print(fav_num)

fav_number()
