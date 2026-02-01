import json
from pathlib import Path

FILE_PATH = Path(__file__).parent.parent / "data"

def write_json(filename: str, data):
    print(data)
    path = FILE_PATH / filename
    
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    
    
def read_json(filename: str):
    path = FILE_PATH / filename
    
    if not path.exists():
        return []
    
    with open(path, "r") as file:
        return json.load(file)