from django.urls import path
from . import views

app_name = 'postapp'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]