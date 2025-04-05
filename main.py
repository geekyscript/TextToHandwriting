from PIL import Image, ImageDraw, ImageFont
import textwrap

# Step 1: Your text input
text = """
Python is amazing! With a few lines of code, my computer writes like a human. 
This is pure magic.
"""

# Step 2: Load a handwriting font (place it in your project folder)
font_path = "DancingScript-VariableFont_wght.ttf"  # You’ll need a handwriting font file here
font_size = 32

# Step 3: Create a blank white image (like paper)
width, height = 700, 1000
background = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(background)

# Step 4: Wrap the text and draw it
font = ImageFont.truetype(font_path, font_size)
margin = 50
offset = 50
for line in textwrap.wrap(text, width=40):
    draw.text((margin, offset), line, font=font, fill="black")
    offset += font_size + 10

# Step 5: Save the output
background.save("handwritten_note.jpg")
print("✅ Handwritten note created locally: handwritten_note.jpg")
