from django.shortcuts import render
from .models import User, Post, Comment
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


# Create your views here.

def index(request):
    
    num_bloggers = User.objects.all().count()

    num_posts = Post.objects.all().count()

    context = {
        'num_bloggers' : num_bloggers,
        'num_posts' : num_posts,
    }

    return render(request, 'index.html', context = context)

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    permission_required = 'blog.add_post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(PermissionRequiredMixin, UpdateView):
    model = Post
    # Not recommended (potential security issue if more fields added)
    fields = ['title', 'content']
    permission_required = 'blog.change_post'

class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    permission_required = 'blog.delete_post'

    def form_valid(self, form):
        pk = self.object.pk

        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("post-delete", kwargs={"pk": pk})
            )
class UserCreate(CreateView):
    model = User
    fields = ['username', 'password', 'email', 'bio']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.password = make_password(
            form.cleaned_data['password']
        )

        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'bio']

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        logout(self.request)
        return super().form_valid(form)

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
        
class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

class PostDetailView(generic.DetailView):
    model = Post

class UserDetailView(generic.DetailView):
    model = User
