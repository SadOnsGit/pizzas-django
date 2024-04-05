from django.shortcuts import render
from index_page.models import Pizzas

def index(request):
    pizzas = Pizzas.objects.all()
    context = {
        'pizzas': pizzas,
    }
    return render(request, 'index.html', context=context)