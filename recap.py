#Python program to check if a number is ODD OR EVEN

num = int(input('Enter a number: '))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print(f'{num} is odd')

