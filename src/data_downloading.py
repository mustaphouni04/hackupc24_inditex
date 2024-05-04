import concurrent.futures
import subprocess
import os
import re
import pandas as pd

def download_image(i, link):
    subprocess.run(["curl", link, "--output", f"data/images/{i}.jpg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def download_images(df, n):
    if not os.path.exists("data/images"):
        os.makedirs("data/images")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(n):
            link = df.iloc[i]["IMAGE_VERSION_1"]
            executor.submit(download_image, i, link)
            
# example usage
# df = pd.read_csv("data/inditextech_hackupc_challenge_images.csv")
# download_images(df, 100)