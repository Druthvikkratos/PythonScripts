import requests # type: ignore

url = "https://github.com/"
file_url = "https://cdn.pixabay.com/photo/2023/11/16/05/02/mountains-8391433_640.jpg"

response = requests.get(file_url)

if response.status_code == 200:
   # with open("example.html","w",encoding="utf-8") as file:
    #    file.write(response.text)
    with open("downloadimage.jpg","wb") as file:
        file.write(response.content)
        print("File downloaded successfully.")
else:
    print(f"Failed to download the web page. Status code: {response.status_code}")