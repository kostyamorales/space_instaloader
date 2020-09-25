import requests
from photo_cropping import resize_images
import argparse
from utils import download_picture


def get_hubble_picture_url(id_pictures):
    images_url = []
    for id_picture in id_pictures:
        url = f'http://hubblesite.org/api/v3/image/{id_picture}'
        response = requests.get(url)
        response.raise_for_status()
        url_image = response.json()['image_files'][-1]['file_url']
        url_image = f'https:{url_image}'
        root = 'image_'
        images_url.append((root, id_picture, url_image))
    return images_url


def get_hubble_collection(collection_name):
    url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(url)
    response.raise_for_status()
    collection = response.json()
    id_pictures = []
    for element in collection:
        id_pictures.append(str(element['id']))
    images_url = get_hubble_picture_url(id_pictures)
    path_name_pictures = download_picture(images_url)
    resize_images(path_name_pictures)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа скачивает коллекцию фотографий hubble и готовит их размер для публикации в instagram'
    )
    parser.add_argument('collection_name', help='название коллекции фотографий hubble')
    args = parser.parse_args()
    hubble_collection_name = args.collection_name

    get_hubble_collection(hubble_collection_name)
