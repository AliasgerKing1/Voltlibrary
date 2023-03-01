import os
import requests
from bs4 import BeautifulSoup
import base64

# Prompt user for website link 
link = str(input("Enter Link: "))

# Prompt user for folder name
folder_name = input("Enter folder name: ")
folder_path = os.path.join("images", folder_name)

# Create folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Prompt user for max number of images to download
max_images = int(input("Enter max number of images to download: "))

# Get list of already downloaded images
downloaded_images = os.listdir(folder_path)
last_index = 0
for image in downloaded_images:
    try:
        index = int(image.split(".")[0][5:])
        if index > last_index:
            last_index = index
    except:
        pass

url = link
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
img_tags = soup.find_all("img")

count = last_index + 1
for img_tag in img_tags:
    if count > max_images:
        break
        
    src = img_tag.get("src")
    if src and src.startswith("http"):
        if src.startswith("data:image/"):
            # Base64-encoded image data
            parts = src.split(",")
            data = parts[1]
            ext = parts[0].split(";")[0][len("data:image/"):]
            filename = f"image{count}.{ext}"
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "wb") as f:
                f.write(base64.b64decode(data))
        else:
            # Image URL
            response2 = requests.get(src)
            ext = src.split(".")[-1].lower()
            if ext in ["jpg", "jpeg", "png", "gif", "webp", "tiff", "psd", "raw", "bmp", "heif", "indd", "svg", "ai", "eps", "pdf"]:
                filename = f"image{count}.{ext}"
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "wb") as f:
                    f.write(response2.content)
        print(f"Saved {filename}")
        count += 1