from django import forms
from .models import Cliente, Produto


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = [
            'nome',
            'cpf',
            'email',
            'telefone',
            'data_nascimento',
            'endereco',
            'cidade',
            'cep'
        ]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto

        fields = ['nome', 'preco']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
        }