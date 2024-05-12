from django.urls import path

from . import views

app_name = 'calculadora'

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página de boas-vindas
    path('calcular_raizes/', views.calcular_raizes, name='calcular_raizes'),
]