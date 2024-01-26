from django.urls import path
from .views import *


app_name = 'blog'


urlpatterns = [
    path('', PostListView.as_view() , name= 'blog_home'),
    path('post_details/<int:pk>', PostDetailView.as_view() , name='blog_single'),
    path('author/<str:username>', PostListView.as_view() , name= 'blog_home_with_username'),
    path('category/<str:cat>', PostListView.as_view() , name= 'blog_home_with_category'),
    path('search/', PostListView.as_view() , name= 'blog_home_with_search'),
]