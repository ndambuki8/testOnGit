#Python program to check if a number is positive begative or o

num = float(input("Type valid number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negtaive")