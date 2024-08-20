import os
import cv2
import openslide
import numpy as np
from matplotlib import pyplot as plt

def get_wsi_files(wsi_folder):
    return [f for f in os.listdir(wsi_folder) if f.endswith('.svs')]

def display_thumbnail(wsi_folder, filename):
    try:
        filepath = os.path.join(wsi_folder, filename)
        print(f"Attempting to open file: {filepath}")
        slide = openslide.OpenSlide(filepath)
        thumbnail = slide.get_thumbnail((slide.dimensions[0] // 20, slide.dimensions[1] // 20))
        thumbnail = cv2.cvtColor(np.array(thumbnail), cv2.COLOR_RGBA2RGB)
        plt.imshow(thumbnail)
        plt.axis('off')
        plt.show()
    except openslide.OpenSlideUnsupportedFormatError as e:
        print(f"Error opening file {filename}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing file {filename}: {e}")

def display_all_thumbnails(wsi_folder):
    files = get_wsi_files(wsi_folder)
    for file in files:
        print(f"Displaying thumbnail for: {file}")
        display_thumbnail(wsi_folder, file)

# Example usage
wsi_folder = 'wsi_images'
display_all_thumbnails(wsi_folder)
