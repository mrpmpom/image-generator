from PIL import Image, ImageDraw, ImageFont
import os

print("Enter the lines you want to draw on the image.")
print("Press ENTER on an empty line to finish.\n")

lines = []
while True:
    line = input("Line: ")
    if line.strip() == "":
        break
    lines.append(line)

width, height = 800, 40 * (len(lines) + 1)  # adjust height based on lines
image = Image.new('RGB', (width, height), color='black')
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()

y_text = 20
for line in lines:
    draw.text((20, y_text), line, font=font, fill='white')
    y_text += 40

base_name = "picture"
ext = ".png"
count = 1

while os.path.exists(f"{base_name}{count}{ext}"):
    count += 1

filename = f"{base_name}{count}{ext}"
image.save(filename)
print("Saved as", filename)
