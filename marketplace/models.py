from django.db import models

# Aqui eu vou programar o modelo
# Classes mapeadas com tabelas
# Persistência
# Orientação a Objetos
# Classe ===> Tabela
# localhost: 8080 - site
# localhost: 8080/admin

class Membro(models.Model):
    email = models.CharField(max_length=50,null=False,blank=False)
    senha = models.CharField(max_length=50,null=False,blank=False)

class Genero(models.Model):
    nome = models.CharField(max_length=50,null=False,blank=False)
    id = models.IntegerField(primary_key=True, blank=False)