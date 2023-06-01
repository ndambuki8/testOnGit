#Python program to check if a number is Prime or not

num = 29

flag = False

if num == 1:
    print(num, "it is not a prime number")
elif num > 1:
    #printing all  factors
    print("factors of num are: ")
    for i in range(2, num +1):
        if (num % i) == 0:
            #if factor is found, set flag to true
            print(f"->{i}\n")
            flag = True
            # break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")