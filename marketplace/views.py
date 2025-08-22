from django.shortcuts import render,redirect
from django.http import HttpResponse
<<<<<<< HEAD
from marketplace.models import Membro
from marketplace.models import Genero
=======
>>>>>>> b1aa38ff449458c3b22cf9996c9820a4fbcff282

def index(request):
    #return HttpResponse("<h1> Alô Senai Games!</h1>")
    # request - requisição
    # template - html entre outros
    # context - objetos (python, python com banco de dados)
    
    
    return render(request,'marketplace/index.html')

<<<<<<< HEAD
def autentica_membro(request):
    """
     dados = {
       1:{"nome":"Visual Novel"}, 
       2:{"nome":"Plataforma"}, 
       3:{"nome":"Acao"}      
    }
    
    """
    dados = Membro.objects.all()
    generos = Genero.objects.all()
   
    return render(request,'marketplace/sou_membro.html',{"cards":dados,"generos":generos})



=======
def autenticar_membro(request):
    dados = {
        1:{"nome":"Visual Novel"},
        2:{"nome":"Plataforma"},
        3:{"nome":"Ação"},
    }
    return render(request,'marketplace/sou_membro.html',{"cards":dados})
>>>>>>> b1aa38ff449458c3b22cf9996c9820a4fbcff282
