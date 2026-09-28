import tomllib

def readToml(path: str):
    with open(path, "rb") as f:
        return tomllib.load(f)

def writeToml(path):
    print("no writing here bud")
