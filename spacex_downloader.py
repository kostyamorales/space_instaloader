import requests
import pathlib
from photo_cropping import resizes_images


def downloads_pictures(picture_url, file_name):
    pathlib.Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(picture_url, verify=False)
    response.raise_for_status()
    file_path = 'images/' + file_name + '.jpg'
    with open(file_path, 'wb') as file:
        file.write(response.content)
        resizes_images(file_path, file_name)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    answer = response.json()
    for number, picture_url in enumerate(answer['links']['flickr_images'], 1):
        downloads_pictures(picture_url, 'spacex_' + str(number))


if __name__ == '__main__':
    fetch_spacex_last_launch()
