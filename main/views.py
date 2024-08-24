from django.shortcuts import render
from django.http import HttpResponse
from django.template import context


from goods.models import Categories


def index(request):



    context = {
        'title': 'Home - главная',
        'content': "Магазин мебели HOME",

    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему наш магазин самый лучший",
    }
       
    return render(request, 'main/about.html', context)
