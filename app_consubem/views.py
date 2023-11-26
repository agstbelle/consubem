from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.POST:
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        usuario = Usuario.objects.filter(user__username=email).first()
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Endereço de e-mail já cadastrado.')
            return render(request, 'cadastro.html')

        # Verificar se o e-mail já está em uso por um objeto Usuario
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Endereço de e-mail já cadastrado.')
            return render(request, 'cadastro.html')

        # Se o usuário e e-mail não existirem, criar um novo usuário
        user = User.objects.create_user(username=email, email=email, password=senha)
        user.save()
        usuario = Usuario(nome=nome, telefone=telefone, user=user, email=email)
        usuario.save()
        messages.success(request, 'Cadastro realizado com sucesso.')
        return redirect('login')
        
    return render(request, 'cadastro.html')

        #if usuario is None:
  
            #user = User.objects.create_user(username=email, email=email, password=senha)
            #user.save()
            #usuario = Usuario(nome=nome, telefone=telefone, user=user)
            #usuario.save()
            #messages.success(request, 'Cadastro realizado com sucesso.')
            #print(messages)
            #return redirect('login')

        #else:
            #print("Usuário já cadastrado")
            #messages.error(request, 'Endereço de e-mail já cadastrado.')
            #return render(request, 'cadastro.html')
            
        
    return render(request, 'cadastro.html')

def user_login(request):
    if request.POST:
        username = request.POST.get('email')
        senha = request.POST['senha']
        user = authenticate(request, username=username, password=senha)
        print(user, username, senha)
        if user is not None:
            login(request, user)
            #return redirect('index')  # Redirecionar para a página após o login
            return redirect("index")
        else:
            messages.error(request, 'usuário ou senha incorretos')
            return render(request, 'login.html')

    return render(request, 'login.html')

def dashboard_admin(request):
    return render(request, 'dashboard_admin.html')

def cadastro_admin(request):
    return render(request, 'cadastrar_admin.html')

def cadastro_produto(request):
    return render(request, 'cadastrar_produto.html')







 






