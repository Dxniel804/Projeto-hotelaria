from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('cadastrar/', views.cadastrar_view, name='cadastrar'),
    path('dashboard_gerente/', views.dashboard_gerente_view, name='dashboard_gerente'),
    path('cadastrar_atendente/', views.cadastrar_atendente_view, name='cadastrar_atendente'),
    path('reservar_quarto/', views.reservar_quarto_view, name='reservar_quarto')
]