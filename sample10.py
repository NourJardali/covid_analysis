file1 = open('numbers.txt', 'r')
numbers = file1.readlines()
even = []
odd = []
multiple = []
for n in numbers:
    num = int(n)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num % 7 == 0:
        multiple.append(num)
print(even)
print(odd)
print(multiple)
