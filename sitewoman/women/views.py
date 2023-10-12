from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import Resolver404

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Главная страница')

def categories(request: HttpRequest, cat_id: str) -> HttpResponse:
    print('cats')
    return HttpResponse(f'''<h1 style="color: red;">Категории:</h1><p>cat_id =  {cat_id} </p>''')

def cats_by_slug(request: HttpRequest) -> HttpResponse:
    query_params = request.GET
    if query_params:
        return HttpResponse('|'.join(list(map(lambda x: f'{x[0]}={x[1]}', query_params.items()))) )
    return HttpResponse(f'''GET is empty</h3>''')


def arhive(request: HttpRequest, year: int) -> HttpResponse:
    if year > 4000:
        raise Http404()
    return HttpResponse(f'''<h3 style="color: green;">Архив:</h3><p>cat_id =  {year} </p>''')


def not_found_404(request: HttpRequest, exception: Resolver404):
    return HttpResponseNotFound("<h2 style='width: 100%; background-color: blue; color: white;'>Page not found</h2>")