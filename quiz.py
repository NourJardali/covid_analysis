def price(num):
    total = num * 5
    if num <= 9:
        return total
    elif num <= 19:
        return total - (total * 0.15)
    else:
        return total - (total * 0.25)

num = int(input("How many boxes of cookies do you want to buy: "))
total = price(num)
print("Your total price = ",total)