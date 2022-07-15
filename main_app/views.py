from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch
from .forms import FeedingForm

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finchees/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finchees_index(request):
  finchees = Finch.objects.all()
  return render(request, 'finchees/index.html', { 'finchees': finchees })

def finchees_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  feeding_form = FeedingForm()
  return render(request, 'finchees/detail.html', {
    'finch': finch, 'feeding_form': feeding_form, 
  })

def add_feeding(request, finch_id):
	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)
