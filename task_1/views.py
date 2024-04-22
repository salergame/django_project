from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    
    context = {
        'title':'Главная',
        'content': 'Это главная страницца моего сайта',
    }
    
    return render(request, 'task_1/index.html',context)

def about(request):
    context = {
        'title':'О сайте',
        'content': 'О сайте',
        'text_on_page':'Здраствуйте меня зовут Санжар и я из Казахстана город Астана до этого я работал с фреймворкам django а также у меня есть проект который опубликован у меня в github  https://github.com/salergame/app1/tree/master я также собираюсь продолжать данный сайт до окончания курса'
    }
    return render(request, 'task_1/about.html', context)

