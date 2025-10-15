import requests
import os
from urllib.parse import urlparse

# Author: Fortune Akioya

def fetch_and_save_image():
    image_url = input("Please enter the URL of the image you want to download: ").strip()

    if not image_url:
        print("Error: No URL provided. Exiting.")
        return

    save_directory = "Fetched_Images"

    try:
        os.makedirs(save_directory, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory '{save_directory}': {e}")
        return

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)
        if not filename or '.' not in filename:
            content_type = response.headers.get('Content-Type', '').lower()
            if 'jpeg' in content_type or 'jpg' in content_type:
                filename = "downloaded_image.jpg"
            elif 'png' in content_type:
                filename = "downloaded_image.png"
            elif 'gif' in content_type:
                filename = "downloaded_image.gif"
            else:
                filename = "downloaded_image.bin"
            
            if '.' not in filename and 'image/' in content_type:
                ext = content_type.split('/')[-1]
                filename = f"downloaded_image.{ext}"

        filename = "".join([c for c in filename if c.isalnum() or c in ('.', '_', '-')]).strip()
        if not filename:
            filename = "downloaded_image_sanitized"

        file_path = os.path.join(save_directory, filename)

        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Image successfully downloaded and saved to '{file_path}'")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}. Status code: {e.response.status_code}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: Could not connect to the URL. Please check your internet connection or the URL. {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: The request timed out. The server might be slow or unresponsive. {e}")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected Request Error occurred: {e}")
    except Exception as e:
        print(f"An unforeseen error occurred: {e}")

if __name__ == "__main__":
    fetch_and_save_image()
