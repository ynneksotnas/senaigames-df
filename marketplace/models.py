from django.db import models

<<<<<<< HEAD
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
=======
# Aqui eu vou programar o modelo
# Classes mapeadas com tabelas
# Persistência
# Orientação a Objetos
# Classe ===> Tabela
# localhost: 8080 - site
# localhost: 8080/admin

>>>>>>> b1aa38ff449458c3b22cf9996c9820a4fbcff282
class Membro(models.Model):
    email = models.CharField(max_length=50,null=False,blank=False)
    senha = models.CharField(max_length=50,null=False,blank=False)
    nome = models.CharField(max_length=80,null=False,blank=False)
<<<<<<< HEAD
    
    def __str__(self):
        return f"Nome [nome={self.nome}]"
    
class Genero(models.Model):
    nome = models.CharField(max_length=90,null=False,blank=False)
    
    def __str__(self):
=======

    def __self__(self):
>>>>>>> b1aa38ff449458c3b22cf9996c9820a4fbcff282
        return f"Nome [nome={self.nome}]"