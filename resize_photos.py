import os
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Ścieżki absolutne (zmień na swoje!)
input_folder = r"Z:\roboty\STABILIZACJA\S19\zdjęcia Sławek\S19_IWONICZ-CZ1-ZDJ+ZES\ZDJECIA-CZ1"
output_folder = r"D:\Python\kuba\web_map\Files\pliki\graniczniki\S19"

# Utwórz folder wyjściowy, jeśli nie istnieje
os.makedirs(output_folder, exist_ok=True)

# Obsługiwane formaty
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            width, height = img.size

            # Skalowanie z zachowaniem proporcji
            if width > height:
                new_width = 800
                new_height = int((800 / width) * height)
            else:
                new_height = 800
                new_width = int((800 / height) * width)

            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            resized_img.save(output_path)

print("Gotowe!")