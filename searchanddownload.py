import os
from serpapi import GoogleSearch
import requests

api_key = "0c77cae9a0fd67e5d99ba38cc8c1686ad3d491c2ecdb1a627787caa38cb75768"
query = "Cute cats"
folder = "downloaded_images"


os.makedirs(folder)

search = GoogleSearch({
    "q": query,
    "api_key": api_key,
    "tbm": "isch"
})

results = search.get_dict()

for index, image in enumerate(results.get("images_results", [])):
    image_url = image["original"]
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(os.path.join(folder, f"image_{index+1}.jpg"), "wb") as file:
            file.write(response.content)
            print(f"Downloaded: {image_url}")