import requests
from bs4 import BeautifulSoup
import os

def download_images(url):
    # Definir el encabezado "User-Agent"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

    # Hacer una solicitud a la URL
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Crear un directorio para guardar las imágenes
    image_dir = 'images'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Encontrar todas las etiquetas img en la página
    images = soup.find_all('img')

    # Descargar y guardar cada imagen
    for i, image in enumerate(images):
        image_url = image.get('src')
        if not image_url.startswith('http'):
            if image_url.startswith('/'):
                image_url = 'https://www.fundacioncnse.org' + image_url
            else:
                image_url = 'https://www.fundacioncnse.org/educa/bancolse/' + image_url

        file_name = os.path.join(image_dir, f'image_{i+1}.jpg')

        try:
            response = requests.get(image_url, headers=headers)
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f'Descargada imagen {i+1} de {len(images)}')
        except requests.exceptions.RequestException as e:
            print(f'Error al descargar la imagen {i+1}: {e}')

# Usar la función para descargar las imágenes
url = 'https://www.fundacioncnse.org/educa/bancolse/dactilologico.php#gsc.tab=0'
download_images(url)