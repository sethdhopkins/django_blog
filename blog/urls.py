from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.PostListView.as_view(), name = 'posts'),
    path('post/<uuid:pk>', views.PostDetailView.as_view(), name = 'post-detail'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name = 'user-detail'),
    path('post/create/', views.PostCreate.as_view(), name='post-create'),
    path('post/<uuid:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('post/<uuid:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name = 'user-detail'),
    path('user/create/', views.UserCreate.as_view(), name='user-create'),
    path('profile/edit/', views.UserUpdate.as_view(), name='profile-update'),
    path('profile/delete/', views.UserDelete.as_view(), name='profile-delete'),
]