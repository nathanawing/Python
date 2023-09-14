import os

# List items to choose from
options = []
for item in os.listdir():
    if os.path.isfile(item):
        options.append(item)
print(options)

# Intake file to read
print("What file do you want to use?")
noFile = True
while noFile == True:
    try:
        file = open(input())
        noFile = False
    except FileNotFoundError:
        (print("File not found."))

phrase = file.read()
file.close()
newPhrase = ""

# List of special characters to exclude
specialChars = [",", ".", "!", "?", "/", "\\", "\'", "\"", " ", "_", ":", ";",
                "+", "-", "=", "$", "%", "&", "(", ")", "[", "]", "{", "}", "@", "#"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Add first letter to new phase
if phrase[0] not in specialChars:
    newPhrase += phrase[0]

# Add the first letter of every word excluding special characters
for i in range(len(phrase)-1):
    if phrase[i] in specialChars and phrase[i] != "\'"\
            and phrase[i+1] not in specialChars and phrase[i+1] not in numbers:
        newPhrase += phrase[i+1]
    elif phrase[i] in numbers:
        newPhrase += phrase[i]

print(newPhrase.lower())
