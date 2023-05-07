#Python program to convert KIlometers to Miles

#Taking the kilometers as input from the user

km = float(input("Enter value in kilometers:"))

#Conversion factor constant
conv_fac = 0.621371

#Calculate miles
miles = km * conv_fac

print("%0.5f kilometers is equal to  %0.5f miles"%(km, miles))