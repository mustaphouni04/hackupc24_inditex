import concurrent.futures
import subprocess
import os
import re
import pandas as pd

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def download_image(name, link):
	img_name = os.path.join(ROOT_PATH, "data", "images", f"{name}.jpg")
	subprocess.run(["curl", link, "--output", img_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def download_images(df, n):
	if not os.path.exists(os.path.join(ROOT_PATH, "data", "images")):
		os.makedirs(os.path.join(ROOT_PATH, "data", "images"))
	with concurrent.futures.ThreadPoolExecutor() as executor:
		for i in range(n):
			for j, v in enumerate(("IMAGE_VERSION_1", "IMAGE_VERSION_2", "IMAGE_VERSION_3")):
				link = df.iloc[i][v]
				executor.submit(download_image, f"{i}_{j}", link)
            
# example usage
if __name__ == "__main__":
	df = pd.read_csv(os.path.join(ROOT_PATH, "data", "inditextech_hackupc_challenge_images.csv"))
	download_images(df, 100)
