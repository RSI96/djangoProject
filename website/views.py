from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

stories = [
    {'id': 1, 'name': 'story 1'},
    {'id': 2, 'name': 'story 2'},
    {'id': 3, 'name': 'story 3'},
]

def home(request):
    return render(request, 'website/home.html')

def about(request):
    context = {'stories': stories}
    return render(request, 'website/about.html', context )

def story(request, pk):
    story = None
    for i in stories:
        if i['id'] == int(pk):
            story = i

    context = {'story':story}
    return render(request, 'website/story.html', context )

def date(request):
    return HttpResponse('current datetime: ' + str(datetime.now()))