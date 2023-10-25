from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/blog.html"
    order_by = "-created_at"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post_detail"
    template_name = "blog/post_detail.html"


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "author", "body"]
    template_name = "blog/post_create.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "body"]
    template_name = "blog/post_update.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post_list")
