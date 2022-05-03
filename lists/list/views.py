from django.http import HttpResponse
from django.shortcuts import render

from list.models import list_of_words


def index(request):
    words = list_of_words.objects.all()
    return render(request, 'list/index.html', {'words' : words})
