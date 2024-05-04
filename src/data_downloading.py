import concurrent.futures
import subprocess
import os
import re
import pandas as pd

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def download_image(name, link, out_dir):
	img_name = os.path.join(out_dir, f"{name}.jpg")
	subprocess.run(["curl", link, "--output", img_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def download_images(df, n, out_dir="data/images"):
	if not os.path.exists(out_dir):
		os.makedirs(out_dir)
	with concurrent.futures.ThreadPoolExecutor() as executor:
		for i in range(n):
			for j, v in enumerate(("IMAGE_VERSION_1", "IMAGE_VERSION_2", "IMAGE_VERSION_3")):
				link = df.iloc[i][v]
				executor.submit(download_image, f"{i}_{j}", link, out_dir)
            
# example usage
if __name__ == "__main__":
	df = pd.read_csv(os.path.join(ROOT_PATH, "data", "inditextech_hackupc_challenge_images.csv"))
	download_images(df, 100, os.path.join(ROOT_PATH, "data", "images"))
