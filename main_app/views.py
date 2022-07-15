from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
  return HttpResponse('<h1>You Are Home...</h1>')

def about(request):
  return render(request, 'about.html')

def finchees_index(request):
  return render(request, 'finchees/index.html', { 'finchees': finchees })