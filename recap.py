#Python program to check if a number is Prime or not

num = 30

flag = False

if num == 1:
    print(num, "it is not a prime number")
elif num > 1:
    #check for factors
    for i in range(2, num):
        if (num % i) == 0:
            #if factor is found, set flag to true
            flag = True
            break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")