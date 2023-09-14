#!/usr/bin/python3

import os

# Set variables
files = []
options = ["txt", "py", "dir", "pdf", "zip", "doc", "ppt", "sh", "yaml"]
extension = ""

# Ask what files type you want
print(options)
print("What file type do you want to use?")
while extension not in options:
	extension = (input())

# Find files with selected extension and add to list
for file in os.listdir():
	if extension == "dir":
		if os.path.isdir(file):
			files.append(file)
	else:
		if file.split(".")[-1] == extension:
			files.append(file)

print(str(len(files)) + " Files with extension: " + extension)
print(files)
