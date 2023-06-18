#Python program to Find the sum of Natral numbers
num = int(input("TYpe upper limit of natural numbers: "))

if num < 0:
    print("Enter a positive number: ")
else:
    sum = 0
    #use while loop to iterate until zero
    while (num > 0):
        sum += num
        num -= 1
    print("THe sum is", sum)