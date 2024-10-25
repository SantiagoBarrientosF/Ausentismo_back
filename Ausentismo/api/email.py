from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.response import Response

def enviar_correo_asesor(subject, body, to_email):
    from_email = settings.EMAIL_HOST_USER
    email = EmailMessage(subject, body, from_email,to_email)
    email.content_subtype = "html"
    email.send()
    
    return Response({"message":"Correo enviado exitosamente"},status=200)

def enviar_correo_lider(subject_lider, body_lider, to_email_asesor):
    from_email = settings.EMAIL_HOST_USER
    email = EmailMessage(subject_lider, body_lider, from_email,to_email_asesor)
    email.content_subtype = "html"
    email.send()
    
    return Response({"message":"Correo enviado exitosamente"},status=200)
