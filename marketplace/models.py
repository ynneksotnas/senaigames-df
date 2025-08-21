from django.db import models

# Aqui eu vou programar o modelo 
# Classes mapeadas com tabelas
# Persistência?
# Orientação a Objetos
# Classe ===> Tabela
# localhost:8080 - site
# localhost:8080/admin
# github
# https://github.com/romulodf-cesar/barbersites/blob/master/crm/models.py

# herança 
class Membro(models.Model):
    email = models.CharField(max_length=50,null=False,blank=False)
    senha = models.CharField(max_length=50,null=False,blank=False)
    nome = models.CharField(max_length=80,null=False,blank=False)
    
    def __str__(self):
        return f"Nome [nome={self.nome}]"
    
class Genero(models.Model):
    nome = models.CharField(max_length=80,null=False,blank=False)
    
    def __str__(self):
        return f"Nome [nome={self.nome}]"