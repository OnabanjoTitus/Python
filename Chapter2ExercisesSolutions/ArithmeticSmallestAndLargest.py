firstNumber = int(input("Enter the first integer"))
smallest = firstNumber
largest = firstNumber
secondNumber = int(input("Enter the second integer"))
thirdNumber = int(input("Enter the third integer"))
if secondNumber > largest:
    largest = secondNumber
if secondNumber < smallest:
    smallest = secondNumber
if thirdNumber > largest:
    largest = thirdNumber
if thirdNumber < smallest:
    smallest = thirdNumber
sum = firstNumber + secondNumber + thirdNumber
product = firstNumber * secondNumber * thirdNumber
average = (firstNumber + secondNumber + thirdNumber)/3
print('the sum is ', sum, 'the average is', average, 'the product is', product, 'the smallest number is ', smallest,
      'and the largest number is', largest)
