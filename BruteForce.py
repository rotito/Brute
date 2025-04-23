import requests

# URL base del servidor web (modifica según tu caso)
base_url = "http://134.209.74.96/"

# Archivo de diccionario con nombres de archivos y carpetas
diccionario_file = "common.txt"

# Leer los elementos del diccionario
with open(diccionario_file, "r", encoding="utf-8") as file:
    elementos = [line.strip() for line in file.readlines()]

# Verificar cada elemento en el servidor
for elemento in elementos:
    url = base_url + elemento
    response = requests.get(url)

    if response.status_code == 200:  # El archivo/carpeta existe
        print(f"[+] Encontrado: {url}")
    elif response.status_code == 403:  # Acceso prohibido, podría existir
        print(f"[!] Posible existencia (403): {url}")
    else:
        pass
    #    print(f"[-] No encontrado: {url}")

print("Escaneo completado.")
