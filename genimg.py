#!/usr/bin/python3 

from PIL import Image, ImageDraw, ImageFont
import sys
import os

os.environ['DISPLAY'] = ':99'

# Input string
# Check if the user provided an input string
if len(sys.argv) < 3:
    print("Usage: python script.py <filename> <input_string>")
    sys.exit(1)

# Input string from command line arguments
filename = sys.argv[1]
input_string = sys.argv[2]

# Create an image with white background
width, height = 7*len(input_string), 30
image = Image.new('RGB', (width, height), color = (255, 255, 255))


# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Define font and size
font = ImageFont.load_default()

# Calculate text width and height to center it
text_width, text_height = draw.textbbox((0, 0), input_string, font=font)[2:4]
position = ((width - text_width) / 2, (height - text_height) / 2)

# Add text to image
draw.text(position, input_string, fill=(0, 0, 0), font=font)

# Save the image
image.save(filename)

