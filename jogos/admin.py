from django.contrib import admin
from .models import Modalidade, Equipe, Tecnico, Atleta

class TecnicoInline(admin.StackedInline):
    model = Tecnico
    extra = 1

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'equipe')
    list_filter = ('modalidades', 'equipe')
    search_fields = ('nome',)

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'quantidade_atletas',)
    list_filter = ('curso',)
    search_fields = ('nome', 'curso')
    inlines = [TecnicoInline]

admin.site.register(Modalidade)