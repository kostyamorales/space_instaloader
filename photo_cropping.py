from pathlib import Path
from math import floor
from PIL import Image
from os import path


def resizes_images(path_name_pictures):
    for path_name_picture in path_name_pictures:
        picture_path, picture_name = path_name_picture
        try:
            image = Image.open(picture_path)
            if image.width / image.height > 1.91:
                image = crops_width_image(image)
            if image.width / image.height < 0.8:
                image = crops_height_image(image)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            image.thumbnail((1080, 1080), Image.ANTIALIAS)
            image.save(Path(f'images/{picture_name}.jpg'), format="JPEG")
            root, ext = path.splitext(picture_path)
            if ext != '.jpg':
                deletes_file(picture_path)
        except Image.UnidentifiedImageError:
            deletes_file(picture_path)
            print(picture_name, 'PIL.UnidentifiedImageError. File deleted.')


def deletes_file(picture_path):
    original_file = Path(picture_path)
    original_file.unlink()


def crops_width_image(image):
    extra_width = image.width - floor(image.height * 1.9)
    x1 = extra_width // 2
    x2 = image.width - x1
    y1 = 0
    y2 = image.height
    cropped_image = image.crop((x1, y1, x2, y2))
    width = floor(image.height * 1.9)
    image = cropped_image.resize((width, image.height))
    return image


def crops_height_image(image):
    extra_height = image.height - image.width // 0.8
    x1 = 0
    x2 = image.width
    y1 = extra_height // 2
    y2 = image.height - y1
    cropped_image = image.crop((x1, y1, x2, y2))
    height = floor(image.width / 0.8)
    image = cropped_image.resize((image.width, height))
    return image
