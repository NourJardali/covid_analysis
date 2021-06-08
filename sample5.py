def calculate_change(val):
    if val == 0:
        print('no change')
    else:
        num10 = val / 10
        val %= 10
        print("10 KD (",int(num10),")")
        num5 = val / 5
        val %= 5
        print("5 KD (",int(num5),")")
        if val >= 1:
            print("1 KD (",int(val),")")
        val %= int(val)
        val *= 1000
        num500 = val / 500
        val %= 500
        print("500 Fils (",int(num500),")")
        num250 = val / 250
        val %= 250
        print("250 Fils (",int(num250),")")
        num100 = val / 100
        val %= 100
        print("100 Fils (",int(num100),")")
        num50 = val / 50
        val %= 50
        print("50 Fils (",int(num50),")")

paid = float(input("Enter amount paid: "))
price = float(input("Enter price: "))
calculate_change(paid - price)