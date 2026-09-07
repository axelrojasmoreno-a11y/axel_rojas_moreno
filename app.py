import os
import shutil

# Cambia esta ruta a la carpeta que contenga tus archivos
CARPETA_ORIGEN = r"C:\Users\axelr\OneDrive\Escritorio\Proyecto 1\logs_entrada"

CARPETAS_DESTINO = {
    "log_app_1": "APP_1",
    "log_app_2": "APP_2",
    "log_app_3": "APP_3"
}

# Validar que la carpeta de origen existe
if not os.path.exists(CARPETA_ORIGEN):
    print(f"Error: La carpeta de origen no existe: {CARPETA_ORIGEN}")
    exit(1)

# Crear las carpetas de destino si no existen
for carpeta in CARPETAS_DESTINO.values():
    ruta_destino = os.path.join(CARPETA_ORIGEN, carpeta)
    os.makedirs(ruta_destino, exist_ok=True)

archivos_clasificados = 0

# Recorrer los archivos de la carpeta de origen
for nombre_archivo in os.listdir(CARPETA_ORIGEN):
    ruta_archivo = os.path.join(CARPETA_ORIGEN, nombre_archivo)

    if not os.path.isfile(ruta_archivo):
        continue

    # Clasificar según la extensión indicada
    for extension, carpeta in CARPETAS_DESTINO.items():
        if extension in nombre_archivo:
            ruta_destino = os.path.join(
                CARPETA_ORIGEN,
                carpeta,
                nombre_archivo
            )

            shutil.move(ruta_archivo, ruta_destino)

            print(f"[OK] {nombre_archivo} -> {carpeta}")

            archivos_clasificados += 1
            break

print(
    f"Proceso finalizado. "
    f"Archivos clasificados: {archivos_clasificados}"
)