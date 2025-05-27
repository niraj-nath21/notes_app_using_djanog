from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import redirect
from .models import data

# Create your views here.

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        name = request.POST.get('name')
        data.objects.create(title=title, content=content, name=name)
        print('Data saved successfully')
        # return redirect('/notes/')
    return render(request, 'index.html')
# This view function handles the request to the index page of the notes app.

def notes(request):
    return render(request, 'notes.html')

def notes_list(request):
    notes = data.objects.all()
    return render(request, 'notes_list.html', {'notes': notes})

def notes_list(request):
    notes = data.objects.all()
    reversed_notes = notes[::-1]  # Reverse the list of notes
    return render(request, 'notes_list.html', {'reversed_notes': reversed_notes,'notes': notes})


