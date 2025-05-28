import pandas as pd
from torch.utils.data import Dataset
from PIL import Image

class PokemonImages(Dataset):
    def __init__(self, csv_file, label, transform = None):
        self.csv = pd.read_csv(csv_file)
        self.transform = transform
        self.label = label
    
    def __len__(self):
        return len(self.csv)
    
    def __getitem__(self,index):
        img_path = self.csv.loc[index, 'image_path']
        label = self.df.loc[index,self.label]

        image = Image.open(img_path).convert("RGB")
        if self.transform:
            image = self.transform(image)

        return image, label