from django import forms
from apps.same.models import ArquivamentoSame

class SameFormCreate(forms.ModelForm):
    class Meta:
        model = ArquivamentoSame

        fields = [
            'created_by',
            'data_atendimento',
            'num_ficha_atendimento',
            'num_prontuario',
            'nome_paciente',
            'data_nascimento',
            'mes_faturamento',
            'data_arquivamento',
            'num_caixa_arquivo',
            'sexo',
            'raca_cor',
            'municipio',
            'tipo_prontuario',
            'upload_prontuario',
        ]

        widgets = {
            'created_by': forms.HiddenInput(),
            'data_atendimento': forms.TextInput(attrs={'data-mask': '00/00/0000'}),
            'num_ficha_atendimento': forms.TextInput(),
            'num_prontuario': forms.TextInput(),
            'nome_paciente': forms.TextInput(),
            'data_nascimento': forms.DateInput(attrs={'data-mask': '00/00/0000'}),
            'mes_faturamento': forms.DateInput(attrs={'data-mask': '00/00/0000'}),
            'data_arquivamento': forms.DateInput(attrs={'data-mask': '00/00/0000'}),
            'num_caixa_arquivo': forms.TextInput(),
            'sexo': forms.Select(),
            'raca_cor': forms.Select(),
            'municipio': forms.TextInput(attrs={'list': 'search'}),
            'tipo_prontuario': forms.Select(),
            'upload_prontuario': forms.FileInput(),
        }
    def __init__(self, user, *args, **kwargs):
        super(SameFormCreate, self).__init__(*args, **kwargs)
        self.fields['created_by'].initial = user



class SameUpadateForm(forms.ModelForm):
    class Meta:
        model = ArquivamentoSame

        fields = [
            'created_by',
            'data_atendimento',
            'num_ficha_atendimento',
            'num_prontuario',
            'nome_paciente',
            'data_nascimento',
            'mes_faturamento',
            'data_arquivamento',
            'num_caixa_arquivo',
            'sexo',
            'raca_cor',
            'municipio',
            'tipo_prontuario',
            'upload_prontuario',
        ]

        widgets = {
            'created_by': forms.HiddenInput(),
            'data_atendimento': forms.TextInput(attrs={'data-mask': '00/00/0000'}),
            'num_ficha_atendimento': forms.TextInput(),
            'num_prontuario': forms.TextInput(),
            'nome_paciente': forms.TextInput(),
            'data_nascimento': forms.DateInput(attrs={'data-mask': '00/00/0000'}),
            'mes_faturamento': forms.DateInput(attrs={'data-mask': '00/00/0000'}),
            'data_arquivamento': forms.DateInput(attrs={'data-mask': '00/00/0000'}),
            'num_caixa_arquivo': forms.TextInput(),
            'sexo': forms.Select(),
            'raca_cor': forms.Select(),
            'municipio': forms.TextInput(attrs={'list': 'search'}),
            'tipo_prontuario': forms.Select(),
            'upload_prontuario': forms.FileInput(),
        }
