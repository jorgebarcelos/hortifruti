from django.shortcuts import render
from produto.models import Produto
from django.core.paginator import Paginator
from produto.forms import PesquisaProdutoForm
from produto.forms import ProdutoForm


def lista_produto(request):
    form = PesquisaProdutoForm(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        lista_de_produtos = Produto.objects.filter(nome__icontains=nome).order_by('nome')
        paginator = Paginator(lista_de_produtos, 3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)

        print(lista_de_produtos)
        print(page_obj)
        return render(request, 'produto/pesquisa_produto.html', {'produtos': page_obj, 'form': form})
    else:
        raise ValueError('Erro ao recuperar produto')


def cadastra_produto(request):

    if request.POST:
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            pass
    else:
        produto_form = ProdutoForm()

    return render(request, 'produto/cadastra_produto.html', {'form': produto_form})
