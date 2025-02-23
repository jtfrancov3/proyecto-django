"""
URL configuration for mi_proyecto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('',views.inicio_view, name='inicio'),
    path('categoria/', views.lista_categorias, name='lista_categorias'),
    path('categoria/crear',views.crear_categoria,name='crear_categoria'),
    path('categoria/<int:categoria_id>/', views.detalle_categoria, name='detalle_categoria'),
    path('categoria/editar/<int:categoria_id>',views.editar_categoria,name='editar_categoria'),
    path('categoria/eliminar_pre/<int:categoria_id>',views.eliminar_categoria_pre,name='eliminar_categoria_pre'),
    path('categoria/eliminar/<int:categoria_id>',views.eliminar_categoria,name='eliminar_categoria'),
]
