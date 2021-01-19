number1 = float(input("Enter the first number"))
number2 = float(input("Enter the second number"))
number3 = float(input("Enter the third number"))
largest = number1
smallest = number1
middle = number1

if number2 > largest:
    largest = number2
if number2 < smallest:
    smallest = number2
if number3 > largest:
    largest = number3
if number3 < smallest:
    smallest = number3

if smallest < number3 < largest:
    middle = number3

if smallest < number2 < largest:
    middle = number2

print(smallest, " is", middle, " is", largest)