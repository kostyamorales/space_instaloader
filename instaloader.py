from instabot import Bot
from os import getenv, listdir, remove
from dotenv import load_dotenv
import time
from shutil import rmtree

load_dotenv()

INSTA_LOGIN = getenv('INSTA_LOGIN')
INSTA_PASSWORD = getenv('INSTA_PASSWORD')


def publication_pictures():
    bot = Bot()
    bot.login(username=INSTA_LOGIN, password=INSTA_PASSWORD)
    try:
        with open("./upload_images.txt", "r", encoding="utf8") as file:
            posted_image_list = file.read().splitlines()
    except Exception:
        posted_image_list = []
    collection = listdir('./images')
    for image in collection:
        if image in posted_image_list:
            continue
        else:
            bot.upload_photo('./images/' + image)
            posted_image_list.append(image)
            with open("./upload_images.txt", "a", encoding="utf8") as file:
                file.write(image + "\n")
        time.sleep(5)
    clean_directories()


def clean_directories():
    for file in listdir('./images'):
        if file[-10:] == '.REMOVE_ME':
            file_path = './images/' + file
            remove(file_path)
    rmtree('./config')


if __name__ == '__main__':
    publication_pictures()
