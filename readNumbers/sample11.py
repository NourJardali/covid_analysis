file1 = open('numbers.txt', 'r')
lines = file1.readlines()
sum = 0
for line in lines:
    currentline = line.split(",")
    for num in currentline:
        sum = sum + int(num)

print(currentline)
print("sum = ",sum)
print("average = ",sum/10)