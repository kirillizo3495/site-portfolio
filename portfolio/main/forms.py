from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput

from .models import Post, Contact





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
            "time_create": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Содержимое:",
            }),

        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = {'name', 'phone_number', 'email', 'message'}
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ваше имя:",
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ваш номер телефона:",
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите электронную почту для связи:",
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Содержимое вашего сообщения:",
            }),
        }