#!/usr/bin/python3 
import sys
import os

# Input string
# Check if the user provided an input string
if len(sys.argv) < 2:
    print("Usage: python script.py <wordsfile>")
    sys.exit(1)

# Input string from command line arguments
filename = sys.argv[1]

# Read the file 'words.txt' and sort the words alphabetically, then print the list

# Open the file in read mode
with open(filename, 'r') as file:
    # Read all lines from the file
    words = file.readlines()

# Strip any leading/trailing whitespace characters from each word
words = [word.strip() for word in words if word.strip()]

# Sort the words alphabetically
words.sort()

# Print the sorted list of words
for w in words:
   print(w)
