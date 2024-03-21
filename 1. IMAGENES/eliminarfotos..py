import os
import shutil

def limit_images_per_folder(parent_folder, limit_per_folder=10):
    # Crear una carpeta para almacenar las carpetas reducidas
    reduced_folder = os.path.join(parent_folder, 'Reduced')
    os.makedirs(reduced_folder, exist_ok=True)

    # Iterar sobre cada carpeta en la carpeta padre
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        # Verificar si es una carpeta
        if os.path.isdir(folder_path):
            # Obtener la lista de archivos en la carpeta
            files = os.listdir(folder_path)
            # Seleccionar solo los primeros 'limit_per_folder' archivos
            files_to_keep = files[:limit_per_folder]
            # Crear una carpeta para almacenar las imágenes limitadas
            limited_folder_path = os.path.join(reduced_folder, f'{folder_name}_limited')
            os.makedirs(limited_folder_path, exist_ok=True)
            # Copiar los archivos seleccionados a la nueva carpeta
            for file in files_to_keep:
                file_path = os.path.join(folder_path, file)
                shutil.copy(file_path, limited_folder_path)

# Especificar la carpeta principal
parent_folder = 'Image'

# Llamar a la función para limitar el número de imágenes por carpeta
limit_images_per_folder(parent_folder)
