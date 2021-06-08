def calculate(price, number, discount):
    total = price * number
    return  total - (total * discount)

N = int(input("Enter number of products: "))
sum = 0.0
for x in range(N):
    price = float(input("Enter price of product: "))
    number = int(input("Enter number of items purchased from the product: "))
    discount = float(input("Enter discount percentage: "))
    sum += calculate(price, number, discount)

print("Total Price = ",sum)
if sum > 100:
    print("Customer will receive a 50% discount during their next visit")