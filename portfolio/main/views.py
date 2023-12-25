
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Work
from django.shortcuts import render, redirect
from .forms import PostForm, ContactForm



def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = PostForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', data)

def pageNotFound(request,exception):
    print(exception)
    return HttpResponseNotFound(f"<h1>Страница не найдена {exception}</h1>")

def ServerError(request):
    return HttpResponseNotFound( '<h1>ошибка сервера<h1>')

def AccessBan(request, exception):
    print(exception)
    return HttpResponseNotFound('<h1>нет доступа<h1>')

def SearchError(request, exception):
    print(exception)
    return HttpResponseNotFound('Ошибка 400')

def index(request) :
    post = Post.objects.order_by('-id')[:1]

    data = {
        'title': 'Главная страница',
        'card': ['категория', 'текст', 'вывод'],
        'post': post,
    }
    return render(request, 'main/index.html', {'data': data})

def contact(request) :
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ContactForm()
    data = {
        'title': 'Связь со мной',
        'form': form,
        'error': error,
    }
    return render(request, 'main/contact.html',  data)

def about(request) :
    post = Post.objects.order_by('-id')[:8]
    data = {
        'title': 'Про нас',
        'post': post,
    }
    return render(request, 'main/about.html', {'data': data})

def portfolio(request):
    posts = Work.objects.all()
    data = {'title': 'Портфолио',
            'posts': posts,
            }
    return render(request, 'main/portfolio.html', data)

def work(request, work_slug):
    post = get_object_or_404(Work, slug=work_slug)
    data = {'title': 'Страница с моей работой',
            'post': post,
            }
    return render(request, 'main/work.html', data)
