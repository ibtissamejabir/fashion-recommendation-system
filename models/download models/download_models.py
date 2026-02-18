
import os
import urllib.request

BASE_URL = "https://github.com/ibtissamejabir/fashion-recommendation-system/releases/download/v1.0-models/"

FILES = [
    "als_model.npz",
    "user_encoder.pkl",
    "item_encoder.pkl",
    "ncf_model.pth"
]

os.makedirs("models", exist_ok=True)

for file in FILES:
    path = os.path.join("models", file)
    if not os.path.exists(path):
        print(f"Downloading {file}...")
        urllib.request.urlretrieve(BASE_URL + file, path)
        print("Done.")
