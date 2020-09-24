import requests
from pathlib import Path
from photo_cropping import resizes_images


def download_picture(images_url):
    Path("images").mkdir(parents=True, exist_ok=True)
    data_files = []
    for number, url in enumerate(images_url, 1):
        response = requests.get(url, verify=False)
        response.raise_for_status()
        file_name = f'spacex_{number}'
        file_path = Path(f'images/{file_name}.jpg')
        data_files.append((file_path, file_name))
        with open(file_path, 'wb') as file:
            file.write(response.content)
    return data_files


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    answer = response.json()
    images_url = []
    for picture_url in answer['links']['flickr_images']:
        images_url.append(picture_url)
    path_name_pictures = download_picture(images_url)
    resizes_images(path_name_pictures)


if __name__ == '__main__':
    fetch_spacex_last_launch()
