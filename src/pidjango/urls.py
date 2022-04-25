"""pidjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from easymngmnt import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 	path('', views.home, name='home'),
 	path('lista_itens/', views.lista_itens, name='lista_itens'),
 	path('add_itens/', views.add_itens, name='add_itens'),
 	path('estoqueupdate/<str:pk>/', views.update_itens, name="estoqueupdate"),
 	path('delete_itens/<str:pk>/', views.delete_itens, name="delete_itens"),
 	path('detalhes/<str:pk>/', views.detalhes, name="detalhes"),
 	path('entrega/<str:pk>/', views.entrega, name="entrega"),
	path('recebi/<str:pk>/', views.recebi, name="recebi"),
	path('aviso/<str:pk>/', views.aviso, name="aviso"),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
