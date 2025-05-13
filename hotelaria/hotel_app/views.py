from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from hotel_app.models import User
from django.contrib.auth.hashers import make_password
from .models import Hospede

# Create your views here.
def homepage_view(request):
    return render(request, 'homepage.html')

def login_view(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('dashboard_gerente')  # Redireciona para o dashboard do gerente
        else:
            messages.error(request, "Email ou senha incorretos!")

    return render(request, 'login.html')

def cadastrar_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')   
        senha = request.POST.get('senha')   
        confirm_senha = request.POST.get('confirm_senha')

        if senha != confirm_senha:
            messages.error(request, 'Senhas não coincidem')
            return redirect('cadastrar')
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email já existe')
            return redirect('cadastrar')
        
        user = User.objects.create(
            username = email,
            email=email,
            password=make_password(senha),  
        )

        user.save( )

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('login')
    
    
    return render(request, 'cadastrar.html')

def dashboard_gerente_view(request):
    return render(request, 'dashboard_gerente.html')

def cadastrar_atendente_view(request):
    return render(request, 'cadastrar_atendente.html')

def reservar_quarto_view(request):
    return render(request, 'reservar_quarto.html')
            
