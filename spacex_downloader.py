import requests
from photo_cropping import resize_images
from utils import download_picture


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    answer = response.json()
    images_url = []
    root = 'spacex_'
    for id_picture, url_image in enumerate(answer['links']['flickr_images'], 1):
        images_url.append((root, id_picture, url_image))
    path_name_pictures = download_picture(images_url)
    resize_images(path_name_pictures)


if __name__ == '__main__':
    fetch_spacex_last_launch()
