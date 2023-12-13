from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

from .models import Comments





class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = {'username', 'comment', 'date'}
        widgets ={
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Пользователь:",
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Комментарий:",
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата:",
            }),
        }
