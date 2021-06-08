names = []
ranks = []
num = int(input("Enter number of faculty members: "))
for i in range(num):
    name = input("Enter name: ")
    print("Choose an academic rank:")
    print("Enter 1 for Assistant Professor")
    print("Enter 2 for Associate Professor")
    print("Enter 3 for Professor")
    rank = int(input("Enter your choice: "))
    names.append(name)
    ranks.append(rank)
subList1 = []
subList2 = []
subList3 = []
for i in range(num):
    if ranks[i] == 1:
        subList1.append(names[i])
    elif ranks[i] == 2:
        subList2.append(names[i])
    else:
        subList3.append(names[i])

print("Assistant Professor: ",sorted(subList1))
print("Associate Professor: ",sorted(subList2))
print("Professor: ",sorted(subList3))