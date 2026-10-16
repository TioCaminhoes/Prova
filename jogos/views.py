from django.shortcuts import render, get_object_or_404
from .models import Modalidade, Equipe, Tecnico, Atleta

def index(request):
    modalidades = Modalidade.objects.all()
    equipes = Equipe.objects.all()
    tecnicos = Tecnico.objects.all()
    atletas = Atleta.objects.all()

    return render(request, 'index.html', {'modalidades': modalidades, 'equipes': equipes, 'tecnicos': tecnicos, 'atletas': atletas})

def modalidade(request, pk):
    modalidades = get_object_or_404(Modalidade, pk=pk)
    equipes = modalidades.atletas.all()
    atletas = modalidades.atletas.all()

    return render(request, 'modalidade.html', {'modalidade': modalidades, 'equipes': equipes, 'atletas': atletas})

def equipe(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    atletas = equipe.atletas.all()
    tecnico = equipe.tecnicos.all()

    return render(request, 'equipe.html', {'equipe': equipe, 'tecnico': tecnico, 'atletas': atletas})
