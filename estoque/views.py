from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Movimentacao
from .forms import MovimentacaoForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listarprodutos.html', {'produtos': produtos})

def movimentacao_estoque(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.produto = produto
            if movimentacao.tipo == 'E':
                produto.quantidade += movimentacao.quantidade
            elif movimentacao.tipo == 'S' and produto.quantidade >= movimentacao.quantidade:
                produto.quantidade -= movimentacao.quantidade
            produto.save()
            movimentacao.save()
            return redirect('listar_produtos')
    else:
        form = MovimentacaoForm()
    return render(request, 'movimentacao_estoque.html', {'produto': produto, 'form': form})
