from PIL import Image
import pathlib
import os


def compress_image(image_path, file_name, folder_path):
    try:
        # Open the image
        with Image.open(image_path) as im:
            # Get the image format
            format = im.format
            if format == "JPEG":
                # Maintain the same quality for JPEG images
                im.save(os.path.join(folder_path, "comp_" +
                        file_name + ".jpg"), format, quality=80)
            elif format == "PNG":
                # Compress PNG images while maintaining the same quality
                im.save(os.path.join(folder_path, "compressed_" +
                        file_name), format, optimize=True)
            else:
                print(
                    f"Cannot compress image {file_name}, format not supported")
    except Exception as e:
        print(f"Error: {e}")


# Compress the image
def compress_images_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    # Iterate over the files
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(folder_path, file)
        # Check if the file is an image
        if file.endswith(('.jpg', '.JPG', '.png', '.jpeg')):
            # Compress the image
            compress_image(file_path, os.path.splitext(file)[0], folder_path)


# Compress all images in the folder
compress_images_in_folder(pathlib.Path("D:/PICS/2021/"))
