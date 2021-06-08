def findIndex(str):
    index = str.find('csc')
    print("The word csc is found at index ",index)

def replaceHashtags(str):
    print(str.replace("#", " "))

def findOccurrence(str):
    print("There are ",str.count('csc')," \'csc\' in this sentence")

def convert(str):
    print(str.title())

#creating options
print("\nMAIN MENU")
print("1. Find the index of the word \"csc\" in a sentence")
print("2. Remove all the \"#\" in sentence")
print("3. Enter a sentence and find the occurrence of a specific word in any sentence")
print("4. Enter any sentence and convert first letter in each word to uppercase")
print("exit to stop")

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        str = input("Enter a sentence: ")
        findIndex(str)
    elif choice == "2":
        str = input("Enter a sentence: ")
        replaceHashtags(str)
    elif choice == "3":
        str = input("Enter a sentence: ")
        findOccurrence(str)
    elif choice == "4":
        str = input("Enter a sentence: ")
        convert(str)
    elif choice == "exit":
        break
    else:
        print("Oops! Incorrect Choice.")