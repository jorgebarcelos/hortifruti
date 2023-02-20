from django import forms
from produto.models import Produto
from categoria.models import Categoria
from config import settings

class PesquisaProdutoForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}), required=False
    )


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria', 'data_cadastro', 'preco', 'qtd_estoque', 'imagem', 'disponivel']

    nome = forms.CharField(
        error_messages = {'required': 'Campo obrigatório', 'unique': 'Nome de produto duplicado'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'})
    )

    descricao = forms.CharField(
        error_messages = {'required': 'Campo obrigatório'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'})
    )

    categoria = forms.ModelChoiceField(
        error_messages = {'required': 'Campo obrigatório'},
        queryset=Categoria.objects.all().order_by('nome'),
        empty_label='--- Selecione uma categoria ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )

    data_cadastro = forms.DateField(
        error_messages = {'required': 'Campo obrigatório', 'invalid': 'Data inválida'},
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm'})
    )