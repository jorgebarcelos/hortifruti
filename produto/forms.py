from django import forms
from produto.models import Produto


class PesquisaProdutoForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlenght': '100'}), required=False
    )


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria', 'data_cadastro', 'preco', 'qtd_estoque', 'imagem', 'disponivel']
