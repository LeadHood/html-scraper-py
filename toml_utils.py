import toml

def readToml(path: str):
    with open(path, "r") as f:
        return toml.load(f)

def writeToml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        toml.dump(data, f)
