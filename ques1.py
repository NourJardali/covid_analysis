list = []
for i in range(5):
    val = int(input("Enter a number"))
    list.append(val)
max = list[0]
min = list[0]
sum = 0
for i in range(5):
    if list[i] < min:
        min = list[i]
    if list[i] > max:
        max = list[i]
    sum = sum + list[i]
print("max = ",max)
print("min = ",min)
print("total = ",sum)
print("first element: ",list[0])
print("second element: ",list[1])
print("third element: ",list[2])
print("last element: ",list[4])
for i in range(2):
    val = int(input("Enter a number"))
    list.append(val)
print("length of list = ",len(list))
list.sort()
print("list after sorting")
for i in list:
    print(i)
print("searching for 5")
for i in list:
    if i == 5:
        print("Found")