from django.shortcuts import render
from blog.models import Post, Author, Tag, Comment
from .forms import CommentForm, PostForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Create your views here.
# These are the posts that will be displayed on the blog page, it will be stored in a database in the future.

def starting_page(request):
    # sorted_posts = sorted(all_posts, key=get_date) # get_date is a callback function that returns the date of each post
    # latest_posts = sorted_posts[-3:]
    latest_posts = Post.objects.all().order_by('-date')[:3] # Django converts the query into an SQL code and it takes into account the limit and offset parameters.
    # We want the latest 3 posts to be displayed on the home page -3:-1 gives us the last 3 posts
    context = {
        'posts': latest_posts
    }
    # context will be passed to the template as a variable
    return render(request, 'blog/index.html', context)

class IndexView(ListView):
    # It fetches all the posts from the database and displays them on the index.html page
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'
    ordering = ['-date']
    # queryset = Post.objects.all().order_by('-date')[:3] # Django converts the query into an SQL code and it takes into account the limit and offset parameters.

class PostListView(ListView):
    # It fetchs all the posts from the database and displays them on the all-posts.html page
    model = Post
    template_name = 'blog/all-posts.html'
    context_object_name = 'all_posts'

def post_detail(request, slug):
    # next is a built-in function that returns the next item in an iterable if it matches a condition
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    identified_post = Post.objects.get(slug=slug) # get the post with the specified slug from the database

    comments = display_comments(request, slug)
    comment_count = comments.count()
    form = CommentForm()
    # retrieve the number of comments there 
    # Add a comment button that make the 
    context = {
        'post': identified_post,
        'post_tags': identified_post.tag.all(), # retrieve all tags associated with the post
        'count': comment_count,
        'form': form,
        'comments' : comments, # retrieve all comments associated with the post
        # 'comment_count': comment_count

    }
    return render(request, 'blog/post-detail.html', context) 

def add_comment(request, slug):
    identified_post = Post.objects.get(slug=slug)
    # form = CommentForm(request.POST)

def display_comments(request, slug):
    identified_post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=identified_post)
    return comments


class createNewPost(CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content', 'author', 'tag']
    template_name = 'blog/create-post.html'
    success_url = reverse_lazy('blog:all-posts')
