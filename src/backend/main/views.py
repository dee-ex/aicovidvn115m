from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .ai import predict
import json

# Create your views here.
@csrf_exempt
def main(request):
    if request.method != "POST":
        return HttpResponse("NOT FOUND")
    
    res = predict(request.FILES["audio"])

    response = {"prob": res}

    return HttpResponse(json.dumps(response), content_type="application/json")
