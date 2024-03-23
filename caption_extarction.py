"""This module extracts captions from images using PyTesseract."""

import pytesseract
from PIL import Image
import os


folder_path = "/give/path/to/folder"


def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text


def extract_text_from_folder(folder_path):
    # Check if the folder path is valid
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    # Define allowed image extensions
    allowed_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff"}

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if file has an allowed extension
        if os.path.splitext(filename)[1].lower() in allowed_extensions:
            file_path = os.path.join(folder_path, filename)

            # Check if it's a file
            if os.path.isfile(file_path):
                print(f"Processing {filename}...")
                extracted_text = extract_text_from_image(file_path)
                print(f"Extracted Text from {filename}:\n{extracted_text}\n")
        else:
            print(f"Skipping non-image file: {filename}")


extract_text_from_folder(folder_path)
