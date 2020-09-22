import requests
from pathlib import Path
from photo_cropping import resize_image
import argparse


def download_picture(images_url):
    Path("images").mkdir(parents=True, exist_ok=True)
    data_files = []
    for image in images_url:
        id, url = image
        pic_expansion = url.split('.')[-1]
        response = requests.get(url, verify=False)
        response.raise_for_status()
        file_name = f'image_{id}'
        file_path = Path(f'images/{file_name}.{pic_expansion}')
        data_files.append((file_path, file_name))
        with open(file_path, 'wb') as file:
            file.write(response.content)
    return data_files


def get_hubble_picture_url(id_pictures):
    images_url = []
    for id in id_pictures:
        url = f'http://hubblesite.org/api/v3/image/{id}'
        response = requests.get(url)
        response.raise_for_status()
        url_image = response.json()['image_files'][-1]['file_url']
        url_image = f'https:{url_image}'
        images_url.append((id, url_image))
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
    data_files = download_picture(images_url)
    resize_image(data_files)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа скачивает коллекцию фотографий hubble и готовит их размер для публикации в instagram'
    )
    parser.add_argument('collection_name', help='название коллекции фотографий hubble')
    args = parser.parse_args()
    hubble_collection_name = args.collection_name

    get_hubble_collection(hubble_collection_name)
