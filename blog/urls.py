from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.PostListView.as_view(), name = 'posts'),
    path('post/<uuid:pk>', views.PostDetailView.as_view(), name = 'post-detail'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name = 'user-detail'),

]