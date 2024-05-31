import requests
import os

def download_file(url: str, local_filename: str):
    """
    Downloads a file from the given URL and saves it locally.

    Args:
        url (str): The URL of the file to download.
        local_filename (str): The local path where the file will be saved.
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ourownstory/neuralprophet-data/main/datasets/energy/SF_hospital_load.csv"
    local_filename = "data/SF_hospital_load.csv"
    
    # Create the data directory if it doesn't exist
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)
    
    # Download the file
    download_file(url, local_filename)
    
    print(f"File downloaded and saved to {local_filename}")