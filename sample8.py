for i in range(3):
    print("Enter how many products customer ",i+1," have bought:")
    n = int(input())
    sum = 0
    for j in range(n):
        print("Enter the price of product ",j+1," for customer ",i+1)
        price = float(input())
        sum += price
    print("The total =",sum)