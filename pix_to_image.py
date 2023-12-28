from PIL import Image

# Read pixel data from the file
with open('pix.txt', 'r') as file:
    lines = file.readlines()
# Convert the pixel data to a list of tuples
pixels = [tuple(map(int, line.strip().split())) for line in lines]
# Calculate the width and height based on the number of pixels
w = 639
h = 726  # You can adjust this based on your file structure

# Create a new image with the specified width and height
image = Image.new("RGB", (h,w))

# Put the pixels into the image
image.putdata(pixels)


flip_img = image.transpose(Image.FLIP_TOP_BOTTOM)
rotate_img = flip_img.transpose(Image.ROTATE_270)
rotate_img.save('b.png')
# Save or display the image
#image.save("my.png")

