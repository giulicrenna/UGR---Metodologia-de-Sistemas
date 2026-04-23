import os
import gdown

DRIVE_FOLDER_URL = "https://drive.google.com/drive/folders/1N_upx66kxNa6MqUD40SsvJqioQLJ8jdm"

folder_id = "1N_upx66kxNa6MqUD40SsvJqioQLJ8jdm"

data_dir = "./data_subte"

os.makedirs(data_dir, exist_ok=True)

print("Descargando archivos históricos del Google Drive...")
print("Este proceso puede tomar algunos minutos.\n")

gdown.download_folder(DRIVE_FOLDER_URL, output=data_dir, quiet=False, use_cookies=False)

print("\nDescarga completada. Archivos disponibles:")
for file in sorted(os.listdir(data_dir)):
    if file.endswith('.csv'):
        file_path = os.path.join(data_dir, file)
        size_mb = os.path.getsize(file_path) / (1024**2)
        print(f"  - {file} ({size_mb:.2f} MB)")