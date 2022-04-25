from django.contrib import admin
from .forms import CriaEstoque

# Register your models here.

from .models import *

class CriaEstoqueAdm(admin.ModelAdmin):
   list_display = ['categoria', 'nome', 'estoque_atual']
   form = CriaEstoque
   search_fields = ['nome', 'categoria']
   list_filter = ['categoria']

admin.site.register(Estoque, CriaEstoqueAdm)
admin.site.register(Categoria)