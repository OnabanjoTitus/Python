from utils import addition, multiplication


def celsius_to_fahrenheit(temperature):
    fahrenheit = addition(multiplication(temperature, 1.8), 32)
    return fahrenheit


celsius = input("Enter your temperature in celsius separated by commas")

allElements = celsius.split(",")

for celsius in allElements:
    temp_cel_val = float(celsius)
    fahrenheits = celsius_to_fahrenheit(temp_cel_val)

    print(f"{temp_cel_val} in celsius is {fahrenheits} ")

