import requests
import pathlib
from photo_cropping import resizes_images
import argparse


def download_picture(picture_url, id_picture, pic_expansion):
    pathlib.Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(picture_url, verify=False)
    response.raise_for_status()
    file_name = 'image_' + id_picture
    file_path = 'images/image_' + id_picture + '.' + pic_expansion
    with open(file_path, 'wb') as file:
        file.write(response.content)
        resizes_images(file_path, file_name)


def get_hubble_picture_url(id):
    url = f'http://hubblesite.org/api/v3/image/{id}'
    response = requests.get(url)
    response.raise_for_status()
    picture_url = 'https:' + response.json()['image_files'][-1]['file_url']
    return picture_url


def get_hubble_collection(collection_name):
    url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(url)
    response.raise_for_status()
    collection = response.json()
    for element in collection:
        id_picture = str(element['id'])
        picture_url = get_hubble_picture_url(id_picture)
        pic_expansion = picture_url.split('.')[-1]
        download_picture(picture_url, id_picture, pic_expansion)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа скачивает коллекцию фотографий hubble и готовит их размер для публикации в instagram'
    )
    parser.add_argument('collection_name', help='название коллекции фотографий hubble')
    args = parser.parse_args()
    hubble_collection_name = args.collection_name

    get_hubble_collection(hubble_collection_name)
