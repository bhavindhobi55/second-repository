import os
from PIL import Image

input_folder = "C:/Users/LENOVO/OneDrive/Pictures/Screenshots/demo/0100300"  # Change this to your folder path
output_folder = "cropped_images"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpeg") or filename.lower().endswith(".jpg"):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        width, height = image.size

        cropped_image = image.crop((0, 0, width, height - 100))

        output_path = os.path.join(output_folder, filename)
        cropped_image.save(output_path)

        print(f"Cropped and saved: {filename}")

print("✅ All images processed successfully!")
