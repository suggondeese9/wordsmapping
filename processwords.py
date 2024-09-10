#!/usr/bin/python3 
import sys
import os
from itertools import permutations, product, chain
from concurrent.futures import ThreadPoolExecutor, as_completed

import subprocess

# Function to run a shell command
def run_shell_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

def process_item(bm, txt, keys, generate):
    print(bm, keys, txt)
    if not generate:
        return None, None
    command = f"./genimg.py {keys}.jpg \"{txt}\""  # Replace with your shell command
    return run_shell_command(command)

def generate_bitmasks(dictionary):
    # Create a list of lists where each sublist contains the bit positions for each key
    bit_positions = []
    current_bit = 0
    for key in dictionary:
        bit_positions.append([(current_bit + i, dictionary[key][i]) for i in range(len(dictionary[key]))])
        current_bit += len(dictionary[key])
    
    # Generate all combinations of bit positions
    for combination in product(*bit_positions):
        bitmask = [0] * current_bit
        selected_keys = []
        selected_values = []
        for pos, value in combination:
            bitmask[pos] = 1
            selected_keys.append(value[0])
            selected_values.append(value[1])
        yield ''.join(map(str, bitmask)), ''.join(selected_values), ''.join(selected_keys)

def generate_bitmasks2(dictionary):
    # Create a list of lists where each sublist contains the bit positions for each key
    bit_positions = []
    current_bit = 0
    for key in dictionary:
        bit_positions.append([(current_bit + i, dictionary[key][i]) for i in range(len(dictionary[key]))])
        current_bit += len(dictionary[key])
    
    # Generate all combinations of bit positions including the possibility of no bit set for each key
    for combination in product(*[chain([(None, None)], positions) for positions in bit_positions]):
        bitmask = [0] * current_bit
        selected_values = []
        for pos, value in combination:
            if pos is not None:
                bitmask[pos] = 1
                selected_values.append(value)
        yield ''.join(map(str, bitmask)), ''.join(selected_values)


# Input string
# Check if the user provided an input string
if len(sys.argv) < 2:
    print("Usage: python script.py <wordsfile>")
    sys.exit(1)

# Input string from command line arguments
filename = sys.argv[1]
generate=True
if '-nogen' in sys.argv:
    generate=False

# Read the file 'words.txt' and sort the words alphabetically, then print the list

# Open the file in read mode
with open(filename, 'r') as file:
    # Read all lines from the file
    words = file.readlines()

words = [word.strip().split(' ') for word in words if word.strip()]

tree = {}
for x in words:
    key = x[0][0]
    word = x[1] if len(x)==2 else ''
    if key not in tree:
        tree[key]=[]
    tree[key].append([x[0], word] )

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = []
    for bm, txt, keys in generate_bitmasks(tree):
        futures.append(executor.submit(process_item, bm, txt, keys, generate))
        
    for future in as_completed(futures):
        output, error = future.result()
        if output:
            print("Output:", output)
        if error:
            print("ERROR:", error)
