from pathlib import Path
import requests


def download_picture(images_url):
    Path("images").mkdir(parents=True, exist_ok=True)
    path_name_pictures = []
    for image in images_url:
        root, id_picture, url = image
        pic_expansion = url.split('.')[-1]
        response = requests.get(url, verify=False)
        response.raise_for_status()
        file_name = f'{root}{id_picture}'
        file_path = Path(f'images/{file_name}.{pic_expansion}')
        path_name_pictures.append((file_path, file_name))
        with open(file_path, 'wb') as file:
            file.write(response.content)
    return path_name_pictures
