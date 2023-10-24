from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/blog.html"
   

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post_detail"
    template_name = "blog/post_detail.html"
