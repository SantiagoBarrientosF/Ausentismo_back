from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.response import Response
from django.template.loader import render_to_string
def enviar_correo_asesor(to_email,solicitudes):
    from_email = settings.EMAIL_HOST_USER
    html_content = render_to_string(
            'Email_template_asesor.html',
            {'solicitud': solicitudes}  # El diccionario permisos se pasa como contexto
        )
    email = EmailMessage(
        subject="Notificación de solicitud de ausentismo",
        body= html_content,
        from_email= from_email,
        to= to_email
        )
    email.content_subtype = "html"
    email.send()
    
    return Response({"message":"Correo enviado exitosamente"},status=200)

def enviar_correo_lider(to_email_asesor,solicitudes):
    from_email = settings.EMAIL_HOST_USER
    html_content = render_to_string(
            'Email_template_lider.html',
            {'solicitud': solicitudes}
    )
    email = EmailMessage(
        subject = "Notificación de solicitud de ausentismo",
        body = html_content, 
        from_email = from_email,
        to= to_email_asesor
    )
    email.content_subtype = "html"
    email.send()
    
    return Response({"message":"Correo enviado exitosamente"},status=200)
