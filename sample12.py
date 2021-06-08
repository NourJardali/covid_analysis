import csv

file = open("temp.csv", "w")
file.write("Fahrenheit" + "\t" + "Celsius" + "\n")
for index in range(-300, 213):
    cel = (5 / 9) * (index - 32)
    file.write(str(index) + "\t" + str(cel) + "\n")
file.close()