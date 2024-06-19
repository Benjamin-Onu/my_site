from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='starting_page'), # or index
    path('posts/', views.PostListView.as_view(), name='posts_page'),
    path('posts/new/', views.createNewPost.as_view(), name='create_post'), # to be implemented
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail_page'),
    path('read_later/', views.ReadLaterView.as_view(), name='read_later'),
    path('search/', views.SearchPostsView.as_view(), name='search_page'), # to be implemented
    # slug is a parameter that will be passed to the view function post_detail
]
