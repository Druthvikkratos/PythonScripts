import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

url = "https://www.google.co.in/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text,"html.parser")
    for link in soup.find_all("a"):
        print(link.get("href"))
else:
    print(f"Failed to fetch the web page. Status code: {response.status_code}")
