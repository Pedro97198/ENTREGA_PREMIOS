import requests
from bs4 import BeautifulSoup

# Obtener el HTML de la página
url = 'file:///C:/Users/Pedro/OneDrive%20-%20Universidad%20Europea%20de%20Madrid/ENTREGA_PREMIOS/documento.html'
response = requests.get(url)

if response.status_code == 200:
    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos los elementos de imagen dentro de los contenedores de carpeta
    imagenes = []
    contenedores_carpeta = soup.find_all('div', class_='folder')
    for contenedor in contenedores_carpeta:
        imagenes_carpeta = contenedor.find_all('img')
        for img in imagenes_carpeta:
            imagenes.append(img['src'])
    
    # Imprimir las rutas de las imágenes
    for img_src in imagenes:
        print(img_src)
else:
    print('Error al obtener la página:', response.status_code)