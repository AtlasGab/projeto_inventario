from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard')

        messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'usuarios/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('dashboard')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'inventario/dashboard.html')


@login_required(login_url='login')
def estoque_view(request):
    return render(request, 'inventario/estoque.html')


@login_required(login_url='login')
def cadastro_material_view(request):
    return render(request, 'inventario/cadastro_material.html')


@login_required(login_url='login')
def entrada_material_view(request):
    return render(request, 'inventario/entrada_material.html')


@login_required(login_url='login')
def retirada_material_view(request):
    return render(request, 'inventario/retirada_material.html')


@login_required(login_url='login')
def emprestimo_view(request):
    return render(request, 'inventario/emprestimo.html')


@login_required(login_url='login')
def devolucao_view(request):
    return render(request, 'inventario/devolucao.html')


@login_required(login_url='login')
def historico_view(request):
    return render(request, 'inventario/historico.html')


@login_required(login_url='login')
def relatorios_view(request):
    return render(request, 'inventario/relatorios.html')


@login_required(login_url='login')
def usuarios_view(request):
    return render(request, 'usuarios/usuarios.html')