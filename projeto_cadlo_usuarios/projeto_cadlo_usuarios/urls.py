from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.login, name='login'),
    path('bem-vindo/', views.bem_vindo, name='bem_vindo'),
    path('editar-usuario/', views.editar_usuario, name='editar_usuario'),
    path('deletar-usuario/', views.deletar_usuario, name='deletar_usuario'),
]
