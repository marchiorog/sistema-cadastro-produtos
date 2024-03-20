from django.shortcuts import render, redirect
from .models import Produto,  Comentario
from .forms import ProdutoForm, ComentarioForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


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
    mensagem_erro = None

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            codigo_produto = form.cleaned_data['codigo_produto']
            comentario_texto = form.cleaned_data['comentario']

            try:
                produto = Produto.objects.get(codigo=codigo_produto)
            except Produto.DoesNotExist:
                mensagem_erro = "O produto não existe. Por favor, insira um código válido."
            else:
                Comentario.objects.create(produto=produto, texto=comentario_texto)
                return redirect('exibir_produto')
    else:
        form = ComentarioForm()

    return render(request, 'cadastro_produtos/comentario.html', {'form': form, 'produto_id': produto_id, 'mensagem_erro': mensagem_erro})

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