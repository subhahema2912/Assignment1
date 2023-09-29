# Reverse the given word
string =  str(input("Enter word:"))
reversed_string = ""
for letter in string:
    reversed_string = letter + reversed_string
print("Reversed word:", reversed_string)