# PROGRAM 7: Count occurrences of each word in a string

text = input("Enter a sentence: ")

words = text.split()       # Split string into words
word_count = {}

for word in words:
    word = word.lower()    # Convert to lowercase for uniform counting
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:")
for w, c in word_count.items():
    print(w, ":", c)
