# PROGRAM 9: Read from a file and count the number of words

filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        print("Total words in the file:", len(words))

except FileNotFoundError:
    print("Error: File not found!")
