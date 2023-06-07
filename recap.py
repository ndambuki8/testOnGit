#Python program to print the fibonacci sequence

nterms = int(input("How many terms? "))

n1, n2 = 0, 1 #first two terms
count = 0

#check if the nuber of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":", n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count+=1
