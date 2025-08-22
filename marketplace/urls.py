# urls exclusivas do aplicativo crud_base
from django.urls import path
from . import views
urlpatterns=[
   path('',views.index,name='index'),
<<<<<<< HEAD
   path('membro/',views.autentica_membro,name='membro'),
 
=======
   path('membro/',views.autenticar_membro,name='membro'),
>>>>>>> b1aa38ff449458c3b22cf9996c9820a4fbcff282
]
