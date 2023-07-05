#LCM using GCD
def compute_gcd(x,y):
    while(y):
          x, y = y, x % y
    return x

def compute_lcm(x, y):
     lcm = (x*y)//compute_gcd(x,y)
     return lcm

num1 = 54
num2 = 24

print("The LCM is", compute_lcm(num1, num2))