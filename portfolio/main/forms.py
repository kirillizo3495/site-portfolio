from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput, forms

from .models import Post, Contact, Work




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


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')

class AddForm(ModelForm):
    class Meta:
        model = Work
        fields = {'title_work', 'text_work', 'img_work', 'slug'}
        widgets = {
            "title_work": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите заголовок:",
            }),
            "text_work": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите текст:",
            }),
            "slug": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите адрес страницы:",
            }),
        }




