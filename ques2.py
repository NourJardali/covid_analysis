list = []
print("enter R for Rainy days")
print("Enter C for cloudy days")
print("Enter S for sunny days")
for i in range(4):
    week = []
    for j in range(3):
        print("For day ",j,"from week ",i)
        status = input("Enter status ")
        week.append(status)
    list.append(week)

totalR = 0
totalC = 0
totalS = 0
totByW = []
for i in range(4):
    r = 0
    c = 0
    s = 0
    week = list[i]
    for j in range(3):
        if week[j] == "R":
            totalR = totalR + 1
            r = r + 1
        elif week[j] == "C":
            totalC = totalC + 1
            c = c + 1
        else:
            totalS = totalS + 1
            s = s + 1
    w = []
    w.append(r)
    w.append(c)
    w.append(s)
    totByW.append(w)
print("Total number of Rainy days in 4 weeks = ",totalR)
print("Total number of Cloudy days in 4 weeks = ",totalC)
print("Total number of Sunny days in 4 weeks = ",totalS)
for i in range (4):
    week = totByW[i]
    print("Total number of Rainy days in week ",i," = ",week[0])
    print("Total number of Cloudy days in week ",i," = ",week[1])
    print("Total number of Sunny days in week ",i," = ",week[2])