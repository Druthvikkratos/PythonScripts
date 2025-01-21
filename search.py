from serpapi import GoogleSearch
import pandas as pd # type: ignore

api_key = "0c77cae9a0fd67e5d99ba38cc8c1686ad3d491c2ecdb1a627787caa38cb75768"

query = "Python Tutorials"

search = GoogleSearch({
    "q": query,
    "location": "India",
    "api_key": api_key
})

results = search.get_dict()

for result in results.get("organic_results", []):
   print(f"Title: {result['title']}")
   print(f"Link: {result['link']}\n")
