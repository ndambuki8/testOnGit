#Python program to display the powers of 2 using anonymous function
terms = 10

#use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are: ", terms)
for i in range(terms):
    print("2 raised to power", i, "is", result[i])