import os
import pandas as pd
import torch
from transformers import AutoModelForImageClassification, AutoFeatureExtractor
from PIL import Image

letras = [chr(i) for i in range(65, 91)]  

datos_imagenes = []


for letra in letras:
    carpeta = f"Image/{letra}"
    for i in range(10): 
        ruta_imagen = f"{carpeta}/{i}.png"
        datos_imagenes.append({"Carpeta": letra, "NombreArchivo": f"{i}.png", "RutaImagen": ruta_imagen})

df_imagenes = pd.DataFrame(datos_imagenes)

model = AutoModelForImageClassification.from_pretrained("RavenOnur/Sign-Language")
feature_extractor = AutoFeatureExtractor.from_pretrained("RavenOnur/Sign-Language")

def clasificar_imagen(ruta_imagen):
    imagen = Image.open(ruta_imagen)

    inputs = feature_extractor(images=imagen, return_tensors="pt")

    outputs = model(**inputs)
    logits = outputs.logits

    predicted_class_idx = logits.argmax().item()
    predicted_class_label = model.config.id2label[predicted_class_idx]

    return predicted_class_label

df_imagenes["ClasePredicha"] = df_imagenes["RutaImagen"].apply(clasificar_imagen)

print(df_imagenes)