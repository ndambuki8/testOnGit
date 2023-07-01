#Python program to find the HCF or GCD using Eucledean algorithm

def compute_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x
hcf = compute_hcf(300,400)
print("hcf is", hcf)