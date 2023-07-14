from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('PROBANDO CORREO DE LABORATORIOGGGAAAA',
              'HOLA AMIGUITO COMO TAS',
              'rchambive@unsa.edu.pe',
              ['rommelchambi8@gmail.com'],
              fail_silently=False)
    return render(request, 'send/index.html')
