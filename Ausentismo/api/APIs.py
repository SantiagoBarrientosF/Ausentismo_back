import requests
from django.conf import settings

# Función para obtener datos de un usuario a través de una API externa, utilizando la 'cedula'
def get_data_api(cedula):
    print("llamando la api..")
    # URL de la API a la que se realiza la solicitud, basada en el valor de 'cedula'
    api_url = f"{settings.EXTERNAL_API_URL}{cedula}"
    headers = {
        "accept": "application/json",
        'Connection': 'keep-alive',
    }
    # Imprime la URL generada para depuración
    print(api_url)
    try:
        # Realiza la solicitud GET a la API con los encabezados definidos
        response = requests.get(api_url, headers=headers)
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
    
def get_data_api_Contratacion(self):
    print("llamando la api..")
    # URL de la API a la que se realiza la solicitud, basada en el valor de 'cedula'
    api_url = f"{settings.EXTERNAL_API_URL_AUSENTISMO}"
    headers = {
        "accept": "application/json",
        'Connection': 'keep-alive',
    }
    # Imprime la URL generada para depuración
    print(api_url)
    try:
        # Realiza la solicitud GET a la API con los encabezados definidos
        response = requests.get(api_url, headers=headers)
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