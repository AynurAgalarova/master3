from .models import Schoder
from django.forms import ModelForm,TextInput,Textarea

class SchoderForm(ModelForm):
    class Meta:
        model = Schoder
        fields = ['title','task']
        widgets = {
            'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Введите текст',
        }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',

        }),

        }
