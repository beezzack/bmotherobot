from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Image


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def image(request, imageid):
    return render(request, 'imageapp/index.html')
