import os
import shutil
import pandas as pd
from PIL import Image

root_dir = 'pokemon_images'  

for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if file_name != '0.jpg' and os.path.isfile(file_path):
                os.remove(file_path)

for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    if os.path.isdir(folder_path):
        old_path = os.path.join(folder_path, '0.jpg')
        new_path = os.path.join(folder_path, f'{folder_name}.jpg')
        if os.path.exists(old_path):
            os.rename(old_path, new_path)

for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)

    if os.path.isdir(folder_path):
        image_filename = f"{folder_name}.jpg"
        image_path = os.path.join(folder_path, image_filename)
        new_path = os.path.join(root_dir, image_filename)

        if os.path.exists(image_path):
            shutil.move(image_path, new_path)  # Move the image to root_dir
        shutil.rmtree(folder_path)  # Delete the subfolder


for item in os.listdir(root_dir):
    item_path = os.path.join(root_dir, item)
    
    # Delete if it's a folder
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)

df = pd.read_csv('meta_info.csv')
print(df.head())

image_folder = "pokemon_images"
for file_name in os.listdir(image_folder):
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(image_folder, file_name)
        with Image.open(path) as img:
            print(f"{file_name}: {img.size}")

input_dir = "pokemon_images"
output_dir = "resized_pokemon_images"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path).convert("RGB")
        img = img.resize((128, 128))  # Resize to 128x128
        img.save(os.path.join(output_dir, filename))