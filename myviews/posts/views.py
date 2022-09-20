from django.views.generic import ListView

# Create your views here.
from .models import Post


class PostPageView(ListView):
    model = Post
    template_name = "posts/posts.html"