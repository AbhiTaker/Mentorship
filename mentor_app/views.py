import json
from django.shortcuts import render
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest

from django.views.decorators.http import require_http_methods

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
@require_http_methods(["OPTIONS", "POST"])
def add_person(request):
    if request.method == 'OPTIONS':
        return HttpResponse(json.dumps({"Message": f"wait"}), content_type='application/json')

    json_body = json.loads(request.body.decode('utf-8'))
    person = Person(name = json_body['name'])
    person.save()

    return HttpResponse(json.dumps({"Message": f"person added"}), content_type='application/json')

@csrf_exempt
@require_http_methods(["OPTIONS", "POST"])
def assign_mentor(request):
    if request.method == 'OPTIONS':
        return HttpResponse(json.dumps({"Message": f"wait"}), content_type='application/json')

    json_body = json.loads(request.body.decode('utf-8'))
    mentor = Person.nodes.get_or_none(name = json_body['mentor'])
    mentee = Person.nodes.get_or_none(name = json_body['mentee'])

    mentor.mentors.connect(mentee)

    return HttpResponse(json.dumps({"Message": f"relationship added"}), content_type='application/json')

@csrf_exempt
@require_http_methods(["GET"])
def get_mentee(request):
    person = request.GET.get('name', None)
    person = mentor = Person.nodes.get_or_none(name = person)
    mentee = person.get_mentee()

    ans = []
    for total in range(0, len(mentee)):
        print(mentee[total].name)
        ans.append(mentee[total].name)
    
    ans = json.dumps(ans)
    return HttpResponse(ans)



    



