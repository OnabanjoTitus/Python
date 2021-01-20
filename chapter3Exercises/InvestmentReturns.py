p = int(input("Enter the amount invested"))
r = int(input("Enter the rate"))
r = 1 + r / 100
a = 0
for years in range(1, 31, 1):
    amount = p * (r ** years)
    a += amount
    print("the total investment in", years, "years", " is", a)
