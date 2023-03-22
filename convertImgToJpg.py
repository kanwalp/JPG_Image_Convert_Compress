import pathlib
from PIL import Image
import os


def convert_image_to_jpg(image_path, folder_path, file_name):
    try:
        # Open the image
        with Image.open(image_path) as im:
            # Save the image as jpeg
            im.save(os.path.join(folder_path, file_name + ".jpg"),
                    format='JPEG', quality=80)
    except Exception as e:
        print(f"Error: {e}")


def convert_images_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    # Iterate over the files
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(folder_path, file)
        # Check if the file is an image
        if file_path.endswith(('.jpg', '.jpeg')):
            # convert the image to jpeg
            convert_image_to_jpg(file_path, folder_path,
                                 os.path.splitext(file)[0])


# convert all images in the folder to jpeg
convert_images_in_folder(pathlib.Path("D:/PICS/HOME/"))
