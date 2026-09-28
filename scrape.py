# Idea: This is just the main program handling everyting
# The cache stores the requested domains, and stores when they were getted last time
# The data is the data that the extractor will handle
# Instead, the cache should store time = something and text = "html string"

import requests
import os
import time

# My own imports
import tomlUtils

cacheDir: str = "./cache/"
domainsFile: str = "./domains.toml"
configFile: str = "./config.toml"

configData = tomlUtils.readToml(configFile)
domainsData = tomlUtils.readToml(domainsFile)

cacheRefreshTime = configData["cacheRefreshTime"]

def clearCache():
    for f in os.scandir(cacheDir):
        if f.is_file():
            os.remove(f)

def handleDomainEntry(entry):
    domain: str = entry["domain"]
    #useCrawl: bool = entry["useCrawler"] -- later implementation in 2.0 ig
    #print("=" * 50)
    print("Handling: " + domain, end= "")
    
    cacheFilePath = cacheDir + domain.replace("/", "_") + ".toml"
    if os.path.exists(cacheFilePath):
        cacheData = tomlUtils.readToml(cacheFilePath)
        if int(time.time() - cacheData["time"]) < cacheRefreshTime:
            print("-- Already cached") 
            return
        print("-- Cached but need a refresh ", end= "")
        
    print("-- Requesting ", end= "")
    response = requests.get(domain)
    
    if response.status_code != 200:
        print("-- Request failed ")
        return

    tomlUtils.writeToml(
        cacheFilePath, 
        {
            "time" : time.time(), 
            "text" : response.text
        }
    ) 

    print("-- Request succeeded and cached ")
    return

def loopThroughEntries():
    for entry in domainsData["domains"]:
        handleDomainEntry(entry)

def configSetup():
    # check if cache dir even exists:
    if not os.path.exists(cacheDir):
        os.makedirs(cacheDir)

    if configData["clearCache"] == True:
        print("Clearing cache...")
        clearCache()

    if configData["cacheRefreshTime"] > 0:
        cacheRefreshTime = int(configData["cacheRefreshTime"])

configSetup()
loopThroughEntries()
