import pathlib
from math import floor
from PIL import Image


def resizes_images(file_path, file_name):
    try:
        image = Image.open(file_path)
        if image.width / image.height > 1.91:
            image = crop_width_images(image)
        if image.width / image.height < 0.8:
            image = crop_height_images(image)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.thumbnail((1080, 1080), Image.ANTIALIAS)
        image.save('images/' + file_name + '.jpg', format="JPEG")
        if file_path[-4:] != '.jpg':
            original_file = pathlib.Path(file_path)
            original_file.unlink()
    except Image.UnidentifiedImageError:
        original_file = pathlib.Path(file_path)
        original_file.unlink()
        print(file_name, 'PIL.UnidentifiedImageError. File deleted.')


def crop_width_images(image):
    extra_width = image.width - floor(image.height * 1.9)
    x1 = extra_width // 2
    x2 = image.width - x1
    y1 = 0
    y2 = image.height
    cropped_image = image.crop((x1, y1, x2, y2))
    width = floor(image.height * 1.9)
    image = cropped_image.resize((width, image.height))
    return image


def crop_height_images(image):
    extra_height = image.height - image.width // 0.8
    x1 = 0
    x2 = image.width
    y1 = extra_height // 2
    y2 = image.height - y1
    cropped_image = image.crop((x1, y1, x2, y2))
    height = floor(image.width / 0.8)
    image = cropped_image.resize((image.width, height))
    return image
