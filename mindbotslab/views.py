"""platzigram views """

# Django
from django.http import HttpResponse
import json

#Utilities
from datetime import datetime

def hello_world(request):
    """return a greeting"""
    return HttpResponse('Oh, hi! Currente server time is {}'.format(
        datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))
    #return HttpResponse('Oh, hi! Currente server time is {}'.format( 
    #    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    #    ))

def sorted_numbers(request):
    """Hi""" 
    #print(request)
    #import pdb;pdb.set_trace() # para poder debugear en la consola
    numbers = request.GET['numbers'].split(',')
    numbers_int = sorted([int(number) for number in numbers])
    data = {
        'status' : 'ok',
        'numbers': numbers_int,
        'message': 'Integers sorted succefully.'
    }
    #response = JsonResponse([numbers_int], safe=False)
    response = HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
        )

    #return HttpResponse(JsonResponse(str(numbers).split(',')))
    return response


def say_hi(request,name,age):
    """return a greatting"""
    if age < 12:
        messague = 'Sorry {} you are not allowed here'.format(name)
    else:
        messague = 'Hi {} welcome to Platzigram '.format(name)

    return HttpResponse(messague)