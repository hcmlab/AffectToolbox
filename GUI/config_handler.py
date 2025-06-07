import json

def deep_update(source: dict, overrides: dict):
    #Recursively updates a nested dictionary `source` with values from `overrides`
    for key, value in overrides.items():
        if isinstance(value, dict) and key in source and isinstance(source[key], dict):
            deep_update(source[key], value)
        else:
            source[key] = value

def load_config(file_path: str) -> dict:
    #Loads a configuration from a JSON file
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            else:
                print("Invalid JSON format: expected a dictionary.")
                return {}
    except Exception as e:
        print(f"Error loading configuration from : {file_path}: {e}")
        return {}

def save_config(file_path: str, config: dict) -> bool:
    #Saves the configuration dictionary to a JSON file
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
        print(f"Configuration saved to {file_path}")
        return True
    except Exception as e:
        print(f"Error saving configuration to {file_path}: {e}")
        return False