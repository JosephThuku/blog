from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post
# Create your views here.
class BlogListView(ListView):
    model=post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = post
    template_name = 'post_detail.html'