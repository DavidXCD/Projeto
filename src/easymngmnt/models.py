from django.db import models

# Create your models here.
categoria_escolha = (
		('Consumível', 'Consumível'),
		('Ferramenta', 'Ferramenta'),
	)

class Categoria(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name
	
class Estoque(models.Model):
	nome = models.CharField(max_length=50, blank=True, null=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	estoque_atual = models.IntegerField(default='0', blank=False, null=True)
	estoque_adicionar = models.IntegerField(default='0', blank=True, null=True)
	fornecedor = models.CharField(max_length=50, blank=True, null=True)
	entrega = models.IntegerField(default='0', blank=True, null=True)
	remover_user = models.CharField(max_length=50, blank=True, null=True)
	destino = models.CharField(max_length=50, blank=True, null=True)
	recebi = models.IntegerField(default='0', blank=True, null=True)
	aviso = models.IntegerField(default='0', blank=True, null=True)
	last_buy = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

def __str__(self):
		return self.nome +' - '+ str(self.estoque_atual)



	