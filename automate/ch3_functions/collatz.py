def collatz(num):
    if num % 2 == 0:
        print(num)
    else:
        print(3 * num + 1)

collatz(5)
