import requests
from django.http import JsonResponse
from rest_framework.views import APIView

# class Backend_data(APIView):
def get_datos_api(request):
     url = "http://127.0.0.1:8001/api/users/"
     
     headers = {
         "accept": "application/json",
         'Connection': 'keep-alive',
     }
     
     try:
         response = requests.get(url,headers=headers)
         if response.status_code == 200:
           print("llamando la api..")
           datos = response.json()
           print(datos)
           return JsonResponse({"data": datos})
         else:
           return JsonResponse("No se pudo conectar")
     except requests.exceptions.RequestException as e:
         print(f"Error: {e}")
         return JsonResponse({"error": str(e)}, status=500)
 
