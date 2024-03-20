from django import forms
from .models import Produto, Comentario


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'altura', 'largura', 'profundidade']

class ComentarioForm(forms.Form):
    codigo_produto = forms.CharField(label='Código do Produto', max_length=100)
    comentario = forms.CharField(label='Comentário', widget=forms.Textarea)
