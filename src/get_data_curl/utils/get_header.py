
import os
import json
from ..model.header import header

def get_header():
    """
        Get header
    """
    name_file = "header.json"
    file_path = os.path.join(os.path.dirname(__file__), ".." ,name_file)

    # Open the JSON file and read its contents
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return header(
        **data
    )