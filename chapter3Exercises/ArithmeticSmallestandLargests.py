number1 = int(input('Enter the number'))
smallest = number1
largest = number1
summing = number1
product = number1
counter = 1
for numbers in range(3):
    number2 = int(input('Enter the number'))
    counter += 1
    summing += number2
    product *= number2
    if number2 > largest:
        largest = number2
    if number2 < smallest:
        smallest = number2
average = summing / counter
print(f'The smallest is {smallest}, and the largest is {largest} the sum is {summing} the product is {product} '
      f'and the average is {average}')
