from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_template, name='main_template'),
    path('games/', views.games, name='games'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('docad/', views.docad, name='docad'),
]
