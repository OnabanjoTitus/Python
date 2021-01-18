p = int(input("Enter the amount invested"))
r = int(input("Enter the rate"))
r = r//100 + 1
n = int(input("Enter the number of years"))
r = r ** n
a = p * r
print("the total investment in ", n, "years", " is ", a)