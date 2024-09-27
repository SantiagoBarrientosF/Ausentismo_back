from django.http import JsonResponse
from rest_framework.views import APIView
import requests
# class Backend_data(APIView):
def get_datos_api(request,cedula):
    print("llamando la api..")
    api_url = f"http://127.0.0.1:8001/api/users/{cedula}"
    headers = {
        "accept": "application/json",
        'Connection': 'keep-alive',
    }
    
    print(api_url )
    try:
        response = requests.get(api_url,headers=headers)
        if response.status_code == 200:
          datos = response.json()
          print(datos)  
          return JsonResponse({"data": datos})
        else:
          return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        # return None