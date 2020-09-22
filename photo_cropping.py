import pathlib
from math import floor
from PIL import Image
from os import path


def resizes_images(data_files):
    for data_file in data_files:
        file_path, file_name = data_file
        try:
            image = Image.open(file_path)
            if image.width / image.height > 1.91:
                image = crop_width_image(image)
            if image.width / image.height < 0.8:
                image = crop_height_image(image)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            image.thumbnail((1080, 1080), Image.ANTIALIAS)
            image.save('images/' + file_name + '.jpg', format="JPEG")
            root, ext = path.splitext(file_path)
            if ext != '.jpg':
                deleted_file(file_path)
        except Image.UnidentifiedImageError:
            deleted_file(file_path)
            print(file_name, 'PIL.UnidentifiedImageError. File deleted.')


def deleted_file(file_path):
    original_file = pathlib.Path(file_path)
    original_file.unlink()


def crop_width_image(image):
    extra_width = image.width - floor(image.height * 1.9)
    x1 = extra_width // 2
    x2 = image.width - x1
    y1 = 0
    y2 = image.height
    cropped_image = image.crop((x1, y1, x2, y2))
    width = floor(image.height * 1.9)
    image = cropped_image.resize((width, image.height))
    return image


def crop_height_image(image):
    extra_height = image.height - image.width // 0.8
    x1 = 0
    x2 = image.width
    y1 = extra_height // 2
    y2 = image.height - y1
    cropped_image = image.crop((x1, y1, x2, y2))
    height = floor(image.width / 0.8)
    image = cropped_image.resize((image.width, height))
    return image
