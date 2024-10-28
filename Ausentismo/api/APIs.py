from django.conf import settings
import aiohttp
import logging
import requests
# Función para obtener datos de un usuario a través de una API externa, utilizando la 'cedula'
async def get_data_api(cedula):
    # URL de la API a la que se realiza la solicitud, basada en el valor de 'cedula'
    api_url = f"{settings.EXTERNAL_API_URL}{cedula}"
    headers = {
        "accept": "application/json",
        'Connection': 'keep-alive',
    }
    # Imprime la URL generada para depuración
    try:
        # Realiza la solicitud GET a la API con los encabezados definidos
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(api_url, headers=headers) as response:
        # Si la respuesta es exitosa (código 200), devuelve los datos en formato JSON
                if response.status == 200:
                    datos = await response.json()
                    return datos
                else:
                    # Si no es exitosa, devuelve 'None'
                    return None
    except aiohttp.ClientError as e:
        # Maneja cualquier error de la solicitud y lo imprime para depuración
        return None
    
async def get_data_api_Gestiones(cedula,tipo_gestion):
    print("llamando la api..")
    # URL de la API a la que se realiza la solicitud, basada en el valor de 'cedula'
    api_url = f"{settings.EXTERNAL_API_URL_AUSENTISMO}{cedula}/{tipo_gestion}/"
    headers = {
        "accept": "application/json",
        'Connection': 'keep-alive',
    }
    # Imprime la URL generada para depuración
    try:
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
        # Realiza la solicitud GET a la API con los encabezados definidos
        # Si la respuesta es exitosa (código 200), devuelve los datos en formato JSON
            async with session.get(api_url, headers=headers) as response:
                if response.status_code == 200:
                    datos = await response.json()
                    print(datos)
                    return datos
                else:
                    # Si no es exitosa, devuelve 'None'
                    return None
    except aiohttp.ClientError as e:
        # Maneja cualquier error de la solicitud y lo imprime para depuración
        return None
    
def get_data_api_all(self):
    print("llamando la api..")
    # URL de la API a la que se realiza la solicitud, basada en el valor de 'cedula'
    api_url = f"{settings.EXTERNAL_API_URL}"
    headers = {
        "accept": "application/json",
        'Connection': 'keep-alive',
    }
    # Imprime la URL generada para depuración
    print(api_url)
    try:
        # Realiza la solicitud GET a la API con los encabezados definidos
        response = requests.get(api_url, headers=headers,timeout=10)
        # Si la respuesta es exitosa (código 200), devuelve los datos en formato JSON
        if response.status_code == 200:
            datos = response.json()
            print(datos)
            return datos
        else:
            # Si no es exitosa, devuelve 'None'
            return None
    except requests.exceptions.RequestException as e:
        # Maneja cualquier error de la solicitud y lo imprime para depuración
        print(f"Error: {e}")
        return None