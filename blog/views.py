from django.shortcuts import render
from blog.models import Post, Author, Tag

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

def posts(request):
    all_posts = Post.objects.all() # retrieve all posts from the database
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog/all-posts.html', context)

def post_detail(request, slug):
    # next is a built-in function that returns the next item in an iterable if it matches a condition
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    identified_post = Post.objects.get(slug=slug) # get the post with the specified slug from the database
    context = {
        'post': identified_post
    }
    return render(request, 'blog/post-detail.html', context) 
