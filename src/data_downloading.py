import concurrent.futures
import subprocess
import os
import re
import pandas as pd

def download_image(name, link):
	subprocess.run(["curl", link, "--output", f"data/images/{name}.jpg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def download_images(df, n):
	if not os.path.exists("data/images"):
		os.makedirs("data/images")
	with concurrent.futures.ThreadPoolExecutor() as executor:
		for i in range(n):
			for j, v in enumerate(("IMAGE_VERSION_1", "IMAGE_VERSION_2", "IMAGE_VERSION_3")):
				link = df.iloc[i][v]
				executor.submit(download_image, f"{i}_{j}", link)
            
# example usage
# df = pd.read_csv("data/inditextech_hackupc_challenge_images.csv")
# download_images(df, 100)