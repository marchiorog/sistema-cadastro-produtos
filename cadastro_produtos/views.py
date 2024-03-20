from django.shortcuts import render, redirect
from .models import Produto,  Comentario
from .forms import ProdutoForm, ComentarioForm
from django.shortcuts import get_object_or_404, redirect

def exibir_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'cadastro_produtos/exibir_produto.html', {'produtos': produtos})

def produto(request):
    if request.method == 'POST':
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            produto = produto_form.save()
            return redirect('exibir_produto')  
    else:
        produto_form = ProdutoForm()
    return render(request, 'cadastro_produtos/produto.html', {'produto_form': produto_form})


def comentario(request, produto_id):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            # Processar o formulário de comentário
            codigo_produto = form.cleaned_data['codigo_produto']
            comentario_texto = form.cleaned_data['comentario']
            # Encontrar o produto pelo código
            produto = Produto.objects.get(codigo=codigo_produto)
            # Criar o comentário associado ao produto
            Comentario.objects.create(produto=produto, texto=comentario_texto)
            # Redirecionar para algum lugar, talvez a página de detalhes do produto
            return redirect('exibir_produto')
    else:
        form = ComentarioForm()
    return render(request, 'cadastro_produtos/comentario.html', {'form': form, 'produto_id': produto_id})

def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('exibir_produto')
    return redirect('exibir_produto')

def deletar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    if request.method == 'POST':
        comentario.delete()
        return redirect('exibir_produto')
    return redirect('exibir_produto')