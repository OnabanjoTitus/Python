age = int(input("Enter your age"))
mbpm = 220-age
targetheartrateminimum = mbpm * 50/100
targetheartratemaximum = mbpm * 85/100
print('Your target heart rate is between', targetheartrateminimum, '-', targetheartratemaximum)