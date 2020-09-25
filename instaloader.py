from instabot import Bot
from os import getenv, listdir, remove, path
from dotenv import load_dotenv
import time
from pathlib import Path
from shutil import rmtree


def publish_pictures():
    bot = Bot()
    bot.login(username=getenv('INSTA_LOGIN'), password=getenv('INSTA_PASSWORD'))
    collection = listdir('images')
    for image in collection:
        bot.upload_photo(Path(f'images/{image}'))
        time.sleep(5)
    clean_directories()


def clean_directories():
    """ Удаляет опубликованные фотографии.

    instabot после публикации фотографии добавляет файлу суффикс '.REMOVE_ME'
    Функция удаляет эти файлы.
    """
    for file_name in listdir('images'):
        root, ext = path.splitext(file_name)
        if ext == '.REMOVE_ME':
            file_path = Path(f'images/{file_name}')
            remove(file_path)


if __name__ == '__main__':
    load_dotenv()

    # удаляет папку './config' при ее наличии. Без этого действия скрипт выдает исключение AssertionError
    if path.isdir('config'):
        rmtree('config')

    publish_pictures()
