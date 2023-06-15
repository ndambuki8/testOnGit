#Python program to Find the sum of Natral numbers
N = int(input("TYpe upper limit of natural numbers: "))

sum = 0

for i in range(0, N+1):
    sum += i

print(sum)