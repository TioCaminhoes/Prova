from django.db import models


class Modalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=20, choices=[('individual', 'Individual'), ('coletivo', 'Coletivo')])
    max_atletas = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'modalidade'
        verbose_name_plural = 'modalidades'

class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    curso = models.CharField(max_length=100)
    cor = models.DecimalField(max_digits=7, decimal_places=0, default='#000000')
    criado_em = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.nome

    def quantidade_atletas(self):
        return self.atletas.count()

    class Meta:
        ordering = ['nome']
        verbose_name = 'equipe'
        verbose_name_plural = 'equipes'

class Tecnico(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='tecnicos')
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'tecnico'
        verbose_name_plural = 'tecnicos'

class Atleta(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name='atletas')
    nome = models.CharField(max_length=100, unique=True)
    matricula = models.CharField(max_length=100, unique=True)
    data_nascimento = models.DateField()
    modalidades = models.ManyToManyField(Modalidade, blank=True, related_name='atletas')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'atleta'
        verbose_name_plural = 'atletas'


