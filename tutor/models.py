from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor')
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome