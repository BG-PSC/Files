from PIL import Image
import os

tile_dir = r"D:\kuba\ortofotodk78\tiles"

for root, dirs, files in os.walk(tile_dir):
    for file in files:
        if file.endswith(".png"):
            img = Image.open(os.path.join(root, file))
            if img.getextrema() == ((0, 0), (0, 0), (0, 0), (0, 0)):  # Wszystkie kanały 0 (czarny)
                os.remove(os.path.join(root, file))  # Usuń czarny tile
                print(f"No data tile {os.path.join(root,file)} deleted")