from django import forms
from .models import Estoque

class CriaEstoque(forms.ModelForm):
   class Meta:
     model = Estoque
     fields = ['categoria', 'nome', 'estoque_atual']

   def limpa_categoria  (self):
            categoria = self.cleaned_data.get('categoria')
            if not categoria:
                    raise forms.ValidationError('Preenchimento obrigatório')
            for itens in Estoque.objects.all():
                if itens.categoria == categoria:
                    raise forms.ValidationError(str(categoria) + ' já existente')
            return categoria

   def limpa_nome(self):
            nome = self.cleaned_data.get('nome')
            if not nome:
                    raise forms.ValidationError('Preenchimento obrigatório')
            for itens in Estoque.objects.all():
                if itens.nome == nome:
                    raise forms.ValidationError(str(nome) + ' já existente')
            return nome

class EstoqueUpdate(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['categoria', 'nome', 'estoque_atual']


class Entrega(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['entrega', 'destino']


class Recebi(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['recebi']

class Aviso(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['aviso']