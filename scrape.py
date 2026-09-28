# Idea: This is just the main program handling everyting
# The cache stores the requested domains, and stores when they were getted last time
# The data is the data that the interpreter will handle

import requests
import os
import tomllib



cacheDir: str = "./cache/"
domainsFile: str = "./domains.toml"

print(readToml(domainsFile))

#for url, directory in subdomains:
    # Making the output more neat
    #print("=" * 50)
    #text = ""
    # See if html is already cached!!
    #if os.path.exists(cacheDirectory + url)
   #     text
        
   # print("Getting" , url, " :")
   # response = requests.get(url)
    
   # if response.status_code != 200:
   #     continue

   # for line in response.text.splitlines():
   #     if "r = " in line: 
   #         print(line)
    
