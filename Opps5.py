# PROGRAM 5: Count vowels and consonants in a string

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():           # Check if character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Total Vowels:", vowel_count)
print("Total Consonants:", consonant_count)
