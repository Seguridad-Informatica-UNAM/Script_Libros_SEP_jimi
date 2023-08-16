import os #proporciona funciones de interaccion con el Sistema operativo
import requests #proporciona funciones para realizar solicitudes http 

# Función para descargar una imagen desde una URL
def descargar_imagen(url, nombre_archivo):
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(respuesta.content)
            print("Imagen descargada exitosamente como", nombre_archivo)
            return True
        else:
            print("Error al descargar la imagen. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", e)
    return False

# Lista de URLs de libros
urls_libros = [
    # Lista de enlaces a los libros
   "https://www.conaliteg.sep.gob.mx/2023/c/P1LPM/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P1TPA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P2MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3LPM/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P3SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P4SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P0CMA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P0SHA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5LPM/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P5SDA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6MLA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6PAA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6PEA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6PCA/",
    "https://www.conaliteg.sep.gob.mx/2023/c/P6SDA/"
]

extension = ".jpg"

# Iterar a través de cada enlace de libro
for base_url in urls_libros:
    # Extraer el nombre del libro del enlace
    nombre_libro = base_url.split("/")[-2]
    
    # Crear una carpeta para el libro si no existe
    carpeta_libro = f"{nombre_libro}/"
    if not os.path.exists(carpeta_libro):
        os.makedirs(carpeta_libro)

    contador = 0
    while True:
        numero_imagen = str(contador).zfill(3) #Convertir contador a cadena de 3 digitos con relleno de ceros
        url_imagen = f"{base_url}{numero_imagen}{extension}" #Construir URL completa de la imagen
        print("Intentando descargar:", url_imagen) 

        nombre_archivo = f"{carpeta_libro}imagen_descargada_{contador}.jpg" #Crear nombre de archivo

        # Intentar descargar la imagen usando la funcion descargar_imagen
        if not descargar_imagen(url_imagen, nombre_archivo):
            break

        contador += 1 #incrementar contador para la siguiente imagen
