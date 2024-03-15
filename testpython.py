from PIL import Image
import os


input_dir = r'c:\Users\mrtab\OneDrive\Desktop\testimages\Для тестового\folder2'
output_path = r'c:\Users\mrtab\OneDrive\Desktop\testimages\result\tiffresults\Results.tif'

# Load all PNG images
images = [Image.open(os.path.join(input_dir, filename)) for filename in os.listdir(input_dir,) if filename.endswith('.png')]


# Define the number of rows and columns
rows = 2
columns = 4

# Calculate the dimensions of the new image
width_max = max(img.width for img in images)
height_max = max(img.height for img in images)
background_width = width_max * columns + (columns - 1) *  100 # Add spacing between columns
background_height = height_max * rows + (rows - 1) * 100  # Add spacing between rows

# Create a new image with the combined width and height
background = Image.new('RGBA', (background_width, background_height), (230, 230, 230, 230))

# Paste each image into the new image at the correct position with spacing
x = 0
y = 0
for i, img in enumerate(images):
    # Calculate the position to paste the image
    x_offset = int((width_max - img.width) / 2)
    y_offset = int((height_max - img.height) / 2)
    # Create a new image with padding
    padded_img = Image.new('RGBA', (width_max, height_max), (230, 230, 230, 230))
    padded_img.paste(img, (x_offset, y_offset))
    background.paste(padded_img, (x, y))
    x += width_max +  100 # Add spacing between columns
    if (i + 1) % columns == 0:
        y += height_max +  100 # Add spacing between rows
        x = 0

# Save the combined image as a TIFF file
background.save(output_path)

print('Conversion finisd')
