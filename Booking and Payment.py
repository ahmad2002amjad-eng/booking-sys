
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def booking(request):
    if request.method == 'POST':
        
        booking_data = request.POST
        if validate_booking_data(booking_data):
            process_payment(booking_data)
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)

def validate_booking_data(data):
    
    return True

def process_payment(data):
 
    pass


SECURE_SSL_REDIRECT = True
def validate_booking_data(data):
    if 'name' not in data or not data['name']:
        return False 
    if 'payment_info' not in data or not data['payment_info']:
        return False  
   
    return True
