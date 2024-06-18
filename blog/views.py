from django.shortcuts import render
from blog.models import Post, Author, Tag, Comment
from .forms import CommentForm, PostForm
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

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
    context_object_name = 'posts' # right now there's no limit to 3 posts,
    # but we can set a limit to 3 posts using the get_queryset method
    ordering = ['-date']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set[:3]
  

class PostListView(ListView):
    # It fetchs all the posts from the database and displays them on the all-posts.html page
    model = Post
    template_name = 'blog/all-posts.html'
    context_object_name = 'all_posts'
    ordering = ['-date']

class PostDetailView(View):
    # It fetches a single post from the database and displays it on the post-detail.html page
    # If the url contains a slug, it will fetch the post with that slug from the database. It will do that automatically.
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get(self, request, slug):
        identified_post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=identified_post)
        context = {
            'post': identified_post,
            'comments': comments,
            'comment_form': CommentForm(),
            'post_tags': identified_post.tag.all(),
            'count' : comments.count()
        }
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        identified_post = Post.objects.get(slug=slug)
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            commentForm.save() # It's a model form, so it saves the data to the database. You don't have to create a new object.
            
            return HttpResponseRedirect(reverse_lazy('blog:post-detail', kwargs={'slug': slug}))
        else:
            return render(request, 'blog/add-comment.html', {'form': form})

    

class addComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add-comment.html'
    success_url = 'blog/posts/' # this should redirect the user to the post-detail page after the comment is added. 
    # but currently it just lists all the posts again.

class createNewPost(CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content', 'author', 'tag']
    template_name = 'blog/create-post.html'
    success_url = reverse_lazy('blog:all-posts')
