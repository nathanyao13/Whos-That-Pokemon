import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Path to your local 'pokemon' folder
image_dir = "pokemon"  # make sure this path is correct relative to your script

# List all image files in the folder
image_files = os.listdir(image_dir)

# Build DataFrame
df = pd.DataFrame({
    "file_name": image_files,
    "file_path": [os.path.join(image_dir, f) for f in image_files]
})

df["Name"] = None  


for idx, row in df.iterrows():
    if pd.notna(row["Name"]):  # Skip already labeled images
        continue

    # Display the image
    img = mpimg.imread(row["file_path"])
    plt.imshow(img)
    plt.axis('off')
    plt.title(f"{row['file_name']} ({idx+1}/{len(df)})")
    plt.show()

    # Ask user for Pokémon name
    name = input("Enter Pokémon name: ").strip()

    df.at[idx, "Name"] = name

    # Save progress every 20 images
    if idx % 20 == 0:
        df.to_csv("labeled_pokemon_progress.csv", index=False)
        print("Progress saved.")