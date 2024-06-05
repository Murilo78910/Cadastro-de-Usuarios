from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroForm, LoginForm, EditarUsuarioForm
from .models import Usuario

def index(request):
    return render(request, 'index.html')

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registrar.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            try:
                usuario = Usuario.objects.get(email=email, senha=senha)
                request.session['usuario_id'] = usuario.id
                return redirect('bem_vindo')
            except Usuario.DoesNotExist:
                form.add_error(None, 'Email ou senha incorretos')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def bem_vindo(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'bem_vindo.html', {'usuario': usuario})

def editar_usuario(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('bem_vindo')
    else:
        form = EditarUsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form})

def deletar_usuario(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('index')
    return render(request, 'deletar_usuario.html', {'usuario': usuario})
