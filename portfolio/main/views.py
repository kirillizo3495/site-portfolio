
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Post , Comments
from django.shortcuts import render, redirect
from .forms import CommentsForm



def create(request):
    error = ''
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = CommentsForm()
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

    comments = Comments.objects.all()
    post = Post.objects.all()

    data = {
        'title': 'Главная страница',
        'card': ['категория', 'текст', 'вывод'],
        'comments': comments,
        'post': post,
    }
    return render(request, 'main/index.html', {'data': data})

def about(request) :
    return render(request, 'main/about.html', {'title': 'Про нас'})

