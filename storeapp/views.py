from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product
# Create your views here.


class index(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = context['product_list']

        return context
