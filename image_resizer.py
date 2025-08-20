import os
from PIL import Image

def resize_images(input_folder, output_folder, width, height):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            img_path = os.path.join(input_folder, file_name)
            img = Image.open(img_path)
            img_resized = img.resize((width, height))
            output_path = os.path.join(output_folder, file_name)
            img_resized.save(output_path)
            print(f"Saved: {output_path}")

# Example call
resize_images("images", "resized", 800, 600)
