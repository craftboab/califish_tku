from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Vendor, Product
from django.views import generic


class IndexView(TemplateView):
    template_name = "califish/index.html"
    # login_url = '/accounts/login/


class ProductList(generic.ListView):
    model = Product
    template_name = "califish/product_list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     products = Product.objects.all().order_by('-created_at')
    #     context = {
    #         'products': products,
    #     }
    #     return context

    def get_queryset(self):
        products = Product.objects.all()
        if 'q' in self.request.GET and self.request.GET['q']!=None:
            q = self.request.GET['q']
            products = products.filter(name__icontains = q)
        return products