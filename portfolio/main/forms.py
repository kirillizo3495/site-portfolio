from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

from .models import Post





class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'text'}
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Заголовок:",
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Содержимое:",
            }),

        }
