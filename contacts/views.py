import requests
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail

@api_view(['POST'])
@authentication_classes([]) # Ignoriamo eventuali cookie di admin
@permission_classes([AllowAny])
def contacts(request):
    dati = request.data
    print("DATI RICEVUTI DA VUE:", dati)

    nome = dati.get('name')
    cognome = dati.get('surname')
    email =  dati.get('email')
    tel = dati.get('telephone')
    messaggio = dati.get('message')
    recaptcha_token = dati.get('recaptcha_token') # <--- AGGIUNTO: Peschiamo il token!

    if not nome or not cognome or not email or not tel or not messaggio:
        return Response ({'error': 'Verifica fallita, dati mancanti'}, status=400)
    
    if not recaptcha_token:
        return Response({'error': 'Token reCAPTCHA mancante. Ricarica la pagina e riprova.'}, status=400)
        
    # 3. VERIFICA CON GOOGLE
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': recaptcha_token
    }
    # Facciamo la "telefonata" a Google
    google_response = requests.post(verify_url, data=payload).json()

    print("RISPOSTA ESATTA DI GOOGLE:", google_response, flush=True)

    # Google ci risponde con un punteggio. Se è < 0.5, è un bot.
    if not google_response.get('success') or google_response.get('score', 0) < 0.5:
        return Response({'error': 'Rilevato traffico anomalo (Bot).'}, status=403)
        
    send_mail(
        subject='Nuovo messaggio dal form contatti',
        message=f'Hai ricevuto un\'Email dal seguente contatto: \n{nome}\n{cognome}\n{email}\n{tel}\n{messaggio}',
        from_email='noreply@tuodominio.com',
        recipient_list=['tuaemail@dominio.com'],
        fail_silently=False
    )
    return Response ({'message': 'Richiesta inviata con successo'}, status=200)