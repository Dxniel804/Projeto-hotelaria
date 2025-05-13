from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

    
class Hospede(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Quarto(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)  # Ex: Simples, Duplo, Suíte
    preco = models.DecimalField(max_digits=8, decimal_places=2)  # Preço por noite
    status = models.CharField(max_length=10, choices=[('livre', 'Livre'), ('reservado', 'Reservado')], default='livre')

class Reserva(models.Model):
    hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

