import os

try:
  import google.colab
  IN_COLAB = True
except:
  IN_COLAB = False

if IN_COLAB:
    PROJECT_DIR = "/content/drive/MyDrive/SyriaWheatWatch"
else:
   PROJECT_DIR = "./SyriaWheatWatch"

DATA_RAW = os.path.join(PROJECT_DIR, "data_raw")
DATA_CLEAN = os.path.join(PROJECT_DIR, "data_clean")
OUTPUTS = os.path.join(PROJECT_DIR, "outputs")

for folder in [PROJECT_DIR, DATA_RAW, DATA_CLEAN, OUTPUTS]:
    os.makedirs(folder, exist_ok=True)

print(f"Project directory: {PROJECT_DIR}")
print(f"Raw data folder:   {DATA_RAW}")
print(f"Clean data folder: {DATA_CLEAN}")
print(f"Outputs folder:    {OUTPUTS}")