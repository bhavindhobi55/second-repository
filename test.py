from PIL import Image

# Open the image
image = Image.open("0100300_1f8291c7.jpeg")

# Get image dimensions
width, height = image.size

# Crop 100 pixels from the bottom
cropped_image = image.crop((0, 0, width, height - 100))

# Save and show the cropped image
cropped_image.save("cropped_image.jpeg")
cropped_image.show()

#    "0100300_4f72487c.jpeg"


import cv2
import numpy as np

# Load the image
image = cv2.imread('image_with_text.jpg')

# Create a mask where the text is located (white for text, black for background)
# You can create this mask manually or use thresholding/edge detection
mask = np.zeros(image.shape[:2], dtype=np.uint8)  # Initialize mask as black

# Define the region where the text is located (e.g., using coordinates or a bounding box)
# Example: Draw a rectangle around the text
x, y, w, h = 100, 50, 200, 30  # Replace with the coordinates of your text
cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)  # Fill the rectangle with white

# Apply inpainting to remove the text
inpainted_image = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# Save or display the result
cv2.imshow('Original Image', image)
cv2.imshow('Inpainted Image', inpainted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------------------------------------------------#------------------------------------------------------------------
import cv2
import numpy as np

# Load the image
image = cv2.imread('0100300_4f72487c.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image. Check the file path.")
    exit()

# Get the height and width of the image
height, width = image.shape[:2]

# Define the source region (a similar part of the image)
# Example: Copy from 100 pixels above the bottom 100 pixels
source = image[height-200:height-100, :].copy()  # Ensure the source is a separate region

# Define the destination region (the text region)
destination = image.copy()  # Work on a copy of the original image

# Create a mask for the text region
mask = np.zeros((100, width), dtype=np.uint8)  # Mask size must match the source region
mask[:, :] = 255  # Set the entire region to white

# Define the center of the destination region
center = (width // 2, height - 50)  # Center of the destination region

# Perform seamless cloning
inpainted_image = cv2.seamlessClone(source, destination, mask, center, cv2.NORMAL_CLONE)

# Save or display the result
cv2.imshow('Original Image', image)
cv2.imshow('Inpainted Image', inpainted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result to a file
cv2.imwrite('image_without_text.jpg', inpainted_image)

