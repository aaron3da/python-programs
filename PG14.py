text = input("Enter a word or phrase: ")

text = text.lower()
text = text.replace(" ", "")

if text == text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
