from django.urls import path
from . import views

# URL Routing in Django
urlpatterns = [
    path('', views.IndexView.as_view(), name='starting_page'), # or index
    path('posts/', views.PostListView.as_view(), name='posts_page'),
    path('posts/new/', views.createNewPost.as_view(), name='create_post'), # to be implemented
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail_page'),
    path('posts/<slug:slug>/edit/', views.EditPostView.as_view(), name='edit_post'), # to be implemented
    path('posts/<str:content>/delete/', views.DeleteObjectView.as_view(), name='delete_object'), # to be implemented
    path('read_later/', views.ReadLaterView.as_view(), name='read_later'),
    path('search/<str:query>/', views.SearchPostsView.as_view(), name='search_page'), # to be implemented
    # slug is a parameter that will be passed to the view function post_detail
]


# A certain URL pattern will represent a database query or a view function. 

'''
EDIT POST TEMPLATE:
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Edit Post Hello World!</title>
</head>

<body>
    <nav>
        <ul>
            <li><a href="/posts">See all posts</a></li>
            <li><a href="/posts/new">Create a Post</a></li>
        </ul>
    </nav>
    <h1>Edit Post Hello World!</h1>
    <form action="/posts/1" method="post">
        <label>Title<input type="text" name="title" value="Hello World!"></label><label>Description <textarea name="description">first post!</textarea></label><button type="submit">Submit</button>
    </form>
</body>

</html>
'''
