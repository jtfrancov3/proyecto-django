from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from .forms import CategoriaForm, LoginForm 
from django.contrib.auth import get_user_model 
from .models import Categoria_Producto

User = get_user_model() 

def login_view(request): 
    if request.method == 'POST': 
        form = LoginForm(request, data=request.POST) 
        if form.is_valid(): 
            username_or_email = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password') 
            
            user = authenticate(request, username=username_or_email, password=password) 
            if not user: 
                try: 
                    user_obj = User.objects.get(email=username_or_email) 
                    user = authenticate(request, username=user_obj.username, password=password) 
                except User.DoesNotExist: 
                    pass 

            if user is not None: 
                login(request, user) 
                return redirect('inicio') 
            else: 
                messages.error(request, 'Usuario o contraseña incorrectos.') 
        else: messages.error(request, 'Datos no válidos.') 
    else:
        form = LoginForm() 
    return render(request, 'usuarios/login.html', {'form': form}) 

@login_required 
def inicio_view(request): 
    return render(request, 'usuarios/inicio.html') 

def logout_view(request): 
    logout(request) 
    #return redirect('login')
    return render(request, 'usuarios/logout.html')

@login_required
def lista_categorias(request):
    categorias = Categoria_Producto.objects.all()

    return render(request, 'usuarios/lista_categorias.html', {'categorias':categorias})

@login_required
def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria_Producto, id = categoria_id)
    productos = categoria.productos.all()

    return render(request, 'usuarios/detalle_categoria.html', {'categoria':categoria, 'productos':productos})


@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'usuarios/crear_categoria.html',{'form':form})

@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria_Producto,id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST,instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'usuarios/editar_categoria.html',{'form':form})


@login_required
def eliminar_categoria_pre(request, categoria_id):
    categoria = get_object_or_404(Categoria_Producto, id = categoria_id)
    productos = categoria.productos.all()

    return render(request, 'usuarios/eliminar_categoria_pre.html', {'categoria':categoria, 'productos':productos})


@login_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria_Producto,id=categoria_id)
    categoria.delete()
    return redirect('lista_categorias')