from django.shortcuts import render

#improt render and response to exchange massage with front-end
from django.http import HttpResponse
from django.shortcuts import render

#improt Category to exchange massage with datebase and model
from rango.models import Category

#improt Page to exchange massage with datebase and model
from rango.models import Page

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'        
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage':'Xuantong Chen'}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        views = Page.views
        context_dict['pages'] = pages
        context_dict['category'] = category
        context_dict['views'] = views

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
        context_dict['views'] = None

    return render(request, 'rango/category.html', context=context_dict)