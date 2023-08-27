
from PIL import Image

# Define the input parameters
img_path = "C:/Users/Emine/Desktop/Python_code/21.tif"
sentinel = "$"

# Open the image and convert it to a 2D array of pixels
img = Image.open(img_path)
pixels = list(img.getdata())
width, height = img.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

# Extract the LSB bitplane
lsb_plane = [[pixel & 1 for pixel in row] for row in pixels]

# Convert the bitplane to a 1D array of bits in column-major order
bits = [lsb_plane[j][i] for i in range(width) for j in range(height)]

# Read the message in column-major order, every 8 bits
message = ""
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    byte_str = "".join(str(bit) for bit in byte)
    byte_ascii = int(byte_str, 2)
    char = chr(byte_ascii)
    message += char
    if char == sentinel:
        break

# Print the message
reversed_message = message[::-1]
print("message: "+ reversed_message)
