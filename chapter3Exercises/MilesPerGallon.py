Total_gallons = 0
Total_miles_Driven = 0

gallons = float(input("Enter the gallons used(-1 to end)"))
milesDriven = float(input("Enter the miles driven:"))
while gallons != -1:
    Total_gallons += gallons
    Total_miles_Driven += milesDriven
    gallons = float(input("Enter the gallons used(-1 to end)"))
    milesDriven = float(input("Enter the miles driven:"))
Total_miles_Driven_Per_Gallons = Total_miles_Driven/Total_gallons
print(f'The overall miles per gallons is {Total_miles_Driven_Per_Gallons}')
