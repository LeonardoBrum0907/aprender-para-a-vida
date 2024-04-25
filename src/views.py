from django.shortcuts import render, Http404, get_object_or_404
from .models import User

def index(request):
      return render(request, 'index.html')

# Create your views here.
