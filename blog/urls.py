from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting_page'), # or index
    path('posts/', views.posts, name='posts_page'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail_page'),
    # slug is a parameter that will be passed to the view function post_detail
]
