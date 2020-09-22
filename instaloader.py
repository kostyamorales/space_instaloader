from instabot import Bot
from os import getenv, listdir, remove, path
from dotenv import load_dotenv
import time
from pathlib import Path
from shutil import rmtree


def publication_pictures():
    bot = Bot()
    bot.login(username=getenv('INSTA_LOGIN'), password=getenv('INSTA_PASSWORD'))
    try:
        with open("upload_images.txt", "r", encoding="utf8") as file:
            posted_image_list = file.read().splitlines()
    except Exception:
        posted_image_list = []
    collection = listdir('images')
    for image in collection:
        if image in posted_image_list:
            continue
        else:
            bot.upload_photo(Path(f'images/{image}'))
            posted_image_list.append(image)
            with open("upload_images.txt", "a", encoding="utf8") as file:
                file.write(f'{image}\n')
        time.sleep(5)
    clean_directories()


# instabot после публикации фотографии добавляет файлу суффикс '.REMOVE_ME'
# Данная функция удаляет файлы, опубликованных фотографий.
def clean_directories():
    for file in listdir('images'):
        root, ext = path.splitext(file)
        if ext == '.REMOVE_ME':
            file_path = Path(f'images/{file}')
            remove(file_path)


if __name__ == '__main__':
    load_dotenv()

    # удаляет папку './config' при ее наличии. Без этого действия скрипт выдает исключение AssertionError
    if path.isdir('config'):
        rmtree('config')

    publication_pictures()
