firstList = {1, 2, 3, 4, 5}
print(firstList)
seconder = {"ace", "ball", "try"}
firstList.append(22)
print(firstList)

firstList.insert(0, 99)
print(firstList)

firstList[0] += 1
print(firstList)

firstList += [66]
print(firstList)

firstList.remove(3)
print(firstList)

firstList.pop()
print(firstList)

seconder.pop()
print(seconder)

secondList = ["Tito", "Titus"]
print(secondList)

thirdList = "-".join(secondList)
print(thirdList)

thirdList = "*".join(secondList)
print(thirdList)

first_int = 10
second_int = 20
if first_int > second_int:
    print("The first int is greater")
else:
    print("The second int is greater")
num = [1, 2, 3, 4, 5]
for spongebob in num:
    print(spongebob)
num = "hello"
for spongebob in num:
    print(spongebob)
for index, spongebob in enumerate(num):
    print(index, spongebob)
for spongebob in num:
    spongebob = 1
    print(spongebob)
for i in range(4):
    print(num[i + 1])
kel = "hello"
for i, j in enumerate(kel[1:], start=1):
    print(i, j)
