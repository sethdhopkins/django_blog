from django.shortcuts import render
from .models import User, Post, Comment
from django.views import generic

# Create your views here.

def index(request):
    
    num_bloggers = User.objects.all().count()

    num_posts = Post.objects.all().count()

    context = {
        'num_bloggers' : num_bloggers,
        'num_posts' : num_posts,
    }

    return render(request, 'index.html', context = context)

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

class PostDetailView(generic.DetailView):
    model = Post

class UserDetailView(generic.DetailView):
    model = User
