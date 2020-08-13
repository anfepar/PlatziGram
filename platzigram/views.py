import pdb;

#Django
from django.http import HttpResponse
from django.http import JsonResponse
#Itulities
from datetime import datetime

def hello_world(request): 
    now = datetime.now() .strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Hi!, current server time is {now}".format(now = str(now)))


def hi(request):
    #pdb.set_trace()
    numbers = sorted(map(lambda x : int(x),request.GET['numbers'].split(",")))
    #numbers = [int(i) for i in request.GET['numbers].split(",")]
    return JsonResponse([numbers], safe=False)

def validate_age(request,name,age):
    if(age < 12):
        message = 'Sorry {}, your not alloowed here'.format(name)
    else:
        message = 'Hello {}, Welcome to Platzigram'.format(name)
    return HttpResponse(message)
