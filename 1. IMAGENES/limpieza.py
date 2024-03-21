import os
import shutil

def filter_images(source_folder, destination_folder):
    # Verificar si la carpeta de origen existe
    if not os.path.exists(source_folder):
        print(f'La carpeta "{source_folder}" no existe.')
        return
    
    print(f'La carpeta "{source_folder}" encontrada.')

    # Crear la carpeta de destino si no existe
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Obtener la lista de archivos en la carpeta de origen
    files = os.listdir(source_folder)
    
    # Filtrar los archivos que terminan con "-SIGNO.png"
    signo_files = [file for file in files if file.endswith('-SIGNO.jpg')]
    
    # Verificar si se encontraron imágenes
    if not signo_files:
        print(f'No se encontraron imágenes que terminen con "-SIGNO.png" en la carpeta "{source_folder}".')
        return
    
    print(f'Se encontraron {len(signo_files)} imágenes que terminan con "-SIGNO.png" en la carpeta "{source_folder}".')
    
    # Copiar los archivos filtrados a la carpeta de destino
    for file in signo_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.copyfile(source_path, destination_path)
        print(f'Copiada imagen {file} a "{destination_folder}"')

# Especificar las carpetas de origen y destino
source_folder = 'images'
destination_folder = 'filtered_images'

# Llamar a la función para filtrar las imágenes y copiarlas
filter_images(source_folder, destination_folder)
