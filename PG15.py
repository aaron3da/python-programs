text = input("Enter a sentence: ")

vowels = 0
words = text.split()

for char in text.lower():
    if char in "aeiou":
        vowels += 1

print("Number of vowels:", vowels)
print("Number of words:", len(words))

print("Character frequency:")

for char in sorted(set(text.lower())):
    if char != " ":
        print(char, ":", text.lower().count(char))
