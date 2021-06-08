def check(n):
    if n >= 50:
        print("1 coupon for each 3 KD")
    elif n >= 25:
        print("1 coupon for each 6 KD")
    else:
        print("1 coupon for each 8 KD")

while True:
    n = int(input("Enter the price of the meal: "))
    if n > 0:
        check(n)
        break