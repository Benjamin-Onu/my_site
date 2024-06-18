from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting_page'), # or index
    path('posts/', views.PostListView.as_view(), name='posts_page'),
    path('posts/new/', views.createNewPost.as_view(), name='create_post'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail_page'),
    path('posts/comment/', views.add_comment, name='add_comment_page')
    # slug is a parameter that will be passed to the view function post_detail
]
