#!/usr/bin/python3 
import sys
import os

# Input string
# Check if the user provided an input string
if len(sys.argv) < 2:
    print("Usage: python script.py <wordsfile> [-i]")
    sys.exit(1)

# Input string from command line arguments
filename = sys.argv[1]
inverse=False
if len(sys.argv)==3 and sys.argv[2]=='-i':
   inverse=True

# Read the file 'words.txt' and sort the words alphabetically, then print the list

# Open the file in read mode
with open(filename, 'r') as file:
    # Read all lines from the file
    words = file.readlines()

for word in words:
    word=word.strip()
    if len(word)==0:
      continue
    word=word.split(' ')
    if len(word)==1:
        word.append('')

    if inverse == False:
      word[1]=word[1].replace('BB','11')
      word[1]=word[1].replace('BJ','22')
      word[1]=word[1].replace('DT','84')
      word[1]=word[1].replace('FS','42')
      word[1]=word[1].replace('CO','32')
      word[1]=word[1].replace('CI','33')
      word[1]=word[1].replace('AT','41')
      word[1]=word[1].replace('FI','31')
      word[1]=word[1].replace('FK','34')
      word[1]=word[1].replace('SO','20')
      word[1]=word[1].replace('QUIR','9999')
      word[1]=word[1].replace('SE','23')
      word[1]=word[1].replace('FE','21')
    else:
      word[1]=word[1].replace('11','BB')
      word[1]=word[1].replace('22','BJ')
      word[1]=word[1].replace('84', 'DT')
      word[1]=word[1].replace('42', 'FS')
      word[1]=word[1].replace('32', 'CO')
      word[1]=word[1].replace('33', 'CI')
      word[1]=word[1].replace('41', 'AT')
      word[1]=word[1].replace('31', 'FI')
      word[1]=word[1].replace('34', 'FK')
      word[1]=word[1].replace('20', 'SO')
      word[1]=word[1].replace('9999', 'QUIR')
      word[1]=word[1].replace('23', 'SE')
      word[1]=word[1].replace('21', 'FE')

    print(f'{word[0]} {word[1]}')    
