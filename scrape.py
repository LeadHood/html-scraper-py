import requests
import os

dataDirectory = "../../data/"
cacheDirectory = "./htmls"

subdomains = [
    ("https://erich-friedman.github.io/packing/cirincir/", "circle"),
    ("https://erich-friedman.github.io/packing/triincir/", "circle"),
    ("https://erich-friedman.github.io/packing/squincir/", "circle"),
    ("https://erich-friedman.github.io/packing/penincir/", "circle"),
    ("https://erich-friedman.github.io/packing/octincir/", "circle"),
    ("https://erich-friedman.github.io/packing/tanincir/", "circle"),
    ("https://erich-friedman.github.io/packing/domincir/", "circle"),
    ("https://erich-friedman.github.io/packing/lincir/", "circle"),
]

# Looping through url and the dir it will be stored in
for url, directory in subdomains:
    # Making the output more neat
    print("=" * 50)
    text = ""
    # See if html is already cached!!
    if os.path.exists(cacheDirectory + url)
        text
        
    print("Getting" , url, " :")
    response = requests.get(url)
    
    if response.status_code != 200:
        continue

    for line in response.text.splitlines():
        if "r = " in line: 
            print(line)
    
