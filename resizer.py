from PIL import Image
import os

input_folder = "datasets"
output_folder = "data"
new_size = (64, 64)

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    # Open and resize the image
    with Image.open(input_path) as img:
        img_resized = img.resize(new_size)

        # Save the resized image to the output folder
        img_resized.save(output_path)