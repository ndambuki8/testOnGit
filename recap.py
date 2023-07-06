#Python program to find the factors of a number

def print_factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = 320

print_factors(num)