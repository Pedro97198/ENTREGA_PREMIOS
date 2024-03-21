import os

def rename_images_in_folders(parent_folder):
    # Iterar sobre cada carpeta en la carpeta principal
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        # Verificar si es una carpeta
        if os.path.isdir(folder_path):
            # Obtener la lista de archivos en la carpeta
            files = os.listdir(folder_path)
            # Renombrar los archivos dentro de la carpeta
            for i, file_name in enumerate(files, start=1):
                # Construir el nuevo nombre del archivo
                new_file_name = f"{folder_name}_{i}.jpg"  # Puedes ajustar la extensión si es necesario
                # Construir la ruta completa del archivo antiguo y nuevo
                old_file_path = os.path.join(folder_path, file_name)
                new_file_path = os.path.join(folder_path, new_file_name)
                # Renombrar el archivo
                os.rename(old_file_path, new_file_path)
                print(f'Renombrado {file_name} a {new_file_name}')

# Especificar la carpeta principal
parent_folder = 'limited'

# Llamar a la función para renombrar las imágenes en cada carpeta
rename_images_in_folders(parent_folder)
