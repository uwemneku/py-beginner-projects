import json


# Save a dictionary to a file path
def save_items(file_path: str, data):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)


# load a dictionary from a file path
def load_items(filepath: str):
    try:
        with open(filepath, "r") as json_file:
            return json.load(json_file)
    except:
        return {}
