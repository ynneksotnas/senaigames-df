from django.shortcuts import render,redirect
from django.http import HttpResponse
from marketplace.models import Membro

def index(request):
    #return HttpResponse("<h1> Alô Senai Games!</h1>")
    # request - requisição
    # template - html entre outros
    # context - objetos (python, python com banco de dados)
    
    
    return render(request,'marketplace/index.html')

def autentica_membro(request):
    """
     dados = {
       1:{"nome":"Visual Novel"}, 
       2:{"nome":"Plataforma"}, 
       3:{"nome":"Acao"}      
    }
    
    """
    dados = Membro.objects.all()
   
    return render(request,'marketplace/sou_membro.html',{"cards":dados})



