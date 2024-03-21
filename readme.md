Proyecto de classificacion de imagenes 
Relaizado por: Ignacio Donderis, Miguel Santiago y Pedro Torrijos

Primera parte (Web Scraping)
    Aqui es donde nos encontramos el primer problema, las fotos que teniamos eran sobre palabras enteras, no sobre las letras en si. Esto no era lo idoneo para crear el modelo.

Segunda parte (Web Scraping)
    Descargamos de una pagina del gobierno con webscraping fotos de el abecedario del lenguaje de signos. Creamos un codigo de python que descarga las fotos otro codigo que etiqueta las palabras segun la etiqueta de la propia web y filtramos para quedarnos unicamente con las fotos que muestran a la persona con su signo. 

Tercera parte (Primer modelo Roboflow)
    Creamos el modelo con las imagenes que hemos sacado que eran un total de 32 imagenes, por consecuencia, al tener tan pocas imagenes el modelo no era funcional dando una precisión demasiado baja.

Cuarta parte (Kaggle)
    Descargamos las imagenes de kaggle con la intención de crear un html, volcar las imagenes en el html y poder hacer el webscraping. Pero este tampoco funciono, por problemas a la hora de crear la pagina web. (Subir imagenes a la pagina web). Por lo que usamos las imagenes directamente.

Quinta parte (EDA)
    Al descargar las imagenes vienen metidas en carpetas por su letra, pero el nombre del png es un numero y no nos servia para luego etiquetar en Roboflow, por lo que creeamos un codigo que utuliza el nombre de esa carpeta para nombrar correctamente las fotos. 
    Al haber limitaciones con el tiempo que tarda roboflow en procesar las imagenes optamos por reducir la cantidad de imagenes por 10 por cada letra.

Sexta parte (Segundo modelo Roboflow)
    Subimos las imagenes las etiquetamos dentro de Roboflow (Asignando 1/3 por persona) y creamos el modelo el cual nos da una precisión de 77.9. Comprobando el modelo con la herramiente que nos proporciona roboflow para usar la camara del movil.

Septima parte (Hugging face)
    Buscamos un modelo preentrenado en la pagina, este clasifica las imagenes en grupos segun el signo.
    https://huggingface.co/RavenOnur/Sign-Language