number = int(input("Enter the number"))
total = 1;
for numbers in range(number, 0, -1):
    total *= numbers
print('the factorial of ', number, 'is ', total)
