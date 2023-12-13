
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

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
    data = {
        'title': 'Главная страница',
        'card': ['категория', 'текст', 'вывод'],
    }
    return render(request, 'main/index.html', data)

def about(request) :
    return render(request, 'main/about.html', {'title': 'Про нас'})
