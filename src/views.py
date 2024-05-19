from django.shortcuts import render, Http404, get_object_or_404
from .models import User
menu = [
      {
            'titulo': 'Home',
            'url': '/'
      },
      {
            'titulo': 'O que fazemos',
            'sub_menu': [
                  {
                        'titulo': 'Bom Samaritano',
                        'url': '/bom-samaritano'
                  }
            ]
      },
      {
            'titulo': 'Como ajudar',
            'sub_menu': [
                  {
                        'titulo': 'Doações',
                        'url': '/doacoes'
                  },
                  {
                        'titulo': 'Voluntários',
                        'url': '/voluntarios'
                  }
            ]
      },
      {
            'titulo': 'Contato',
            'url': '/contato'
      },
]
def index(request):
      return render(request, 'aprender_para_vida/index.html', {'menu': menu})
def bom_samaritano(request):
      return render(request, 'aprender_para_vida/bom-samaritano.html', {'menu': menu})
def doacoes(request):
      return render(request, 'aprender_para_vida/doacoes.html', {'menu': menu})
def voluntarios(request):
      return render(request, 'aprender_para_vida/voluntarios.html', {'menu': menu})
def contato(request):
      return render(request, 'aprender_para_vida/contato.html', {'menu': menu})
def base(request):
      return render(request, 'aprender_para_vida/base.html', {'menu': menu})