from django.dispatch import Signal
user_logged_in = Signal()
user_login_failed = Signal()
user_logged_out = Signal()


url = "http://127.0.0.1:8001"

def getcwd()-> str:
     return "Exito"
