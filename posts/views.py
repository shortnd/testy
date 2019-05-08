from django.views.generic import ListView
from django.shortcuts import render

from .models import Post

class PostPageView(ListView):
  model = Post
  template_name = "posts.html"
