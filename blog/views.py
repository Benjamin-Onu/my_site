from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from blog.models import Post, Comment
from .forms import CommentForm, PostForm
from django.views import View
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView

from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
# These are the posts that will be displayed on the blog page, it will be stored in a database in the future.

class IndexView(ListView):
    # It fetches all the posts from the database and displays them on the index.html page
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts' 
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

    def is_stored_post(self, request, post_id):
        stored_post = request.session.get('stored_posts')
        # This is to check if the post is saved for later. It will check if the post id is in the stored_post list in the session. Therefore won't display the save for later button if the post is already saved for later.
        if stored_post is not None:
            is_saved_for_later = post_id in stored_post
        else:
            is_saved_for_later = False
        return is_saved_for_later
    
    def get(self, request, slug):
        identified_post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=identified_post)
        is_saved_for_later = self.is_stored_post(request, identified_post.id)

        context = {
            'post': identified_post,
            'comments': comments,
            'comment_form': CommentForm(),
            'post_tags': identified_post.tag.all(),
            'count' : comments.count(),
            'is_saved_for_later': is_saved_for_later
        }
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        '''Once the form is submitted, it will run this method and the slug will be part of the url. It's specified in the action attribute of the form in the template. '''
        commentForm = CommentForm(request.POST)
        identified_post = Post.objects.get(slug=slug)
        if commentForm.is_valid():
            # Before saving it to the database, we need to define the post object it is being commented on
            
            comment = commentForm.save(commit=False) # We create a new object without saving it to the database
            comment.post = identified_post
            commentForm.save() # It's a model form, so it saves the data to the database. You don't have to create a new object.
            return HttpResponseRedirect(reverse('post_detail_page', args=[slug]))
        
        # If the form is not valid, it will display the form with the errors
        comments = Comment.objects.filter(post=identified_post).order_by('-date')
        is_saved_for_later = self.is_stored_post(request, identified_post.id)

        context = {
            'post': identified_post,
            'comments': comments,
            'comment_form': commentForm, # It will display the form with the errors
            'post_tags': identified_post.tag.all(),
            'count' : comments.count(),
            'is_saved_for_later': is_saved_for_later
        }

        return render(request, self.template_name, context)

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        # If the post is already saved for later, it will remove it from the list. Otherwise, it will add it to the list.
        # As the button is set based on if the post is saved for later or not, it will update the button accordingly.
        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")


# To be implemented in the future
class createNewPost2(CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content', 'author', 'tag']
    template_name = 'blog/create-post.html'
    success_url = '/blog/all-posts.html'
    # reverse_lazy is used to avoid circular import. It will redirect to the posts_page after the post is created.

class createNewPost(View):
    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog/create-post.html', context)

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        # image is the issue here 
        print(request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.image_name = request.FILES['image_name']
            # post.author = request.user # By default, it will set the author to the current user.
            # request.user.post_set.add(post)
            form.save()
            '''
            from django.contrib.auth.decorators import login_required

            from django.cntrib.auth.models import User, auth
            from django.contirb import messages

            @login_required
            def add_post_preview(request):
                if request.method == 'POST':
                    form = PostForm(request.POST, request.FILES)
                    if form.is_valid():
                        post = form.save(commit=False)
                        post.image_name = request.FILES['image']
                        post.author = request.user
                        request.user.post_set.add(post)
                        post.save()
                        return redirect('add_post_preview')
                    else:
                        context = {'form': form }
                        return render(request, 'blog/create-post.html', context)
                else:
                    form = PostForm()
                    context = {
                        'form': form
                    }
                    return render(request, 'blog/create-post.html', context)
            
            '''
            return HttpResponseRedirect(reverse('posts_page'))
        else:
            context = {'form': form }
            return render(request, 'blog/create-post.html', context)



# To be implemented in the future
class SearchPostsView(View):
    # db_index will be key to search in the database. It will be used to improve the search performance.
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'search_results'

    # The search query will be passed as a GET parameter in the url.
    # the key will be 'query' and the value will be the search query. 'query' will be the name of the input field in the form.
    def get(self, request, query):
        query = request.GET.get('query')
        # What if the query is a request from AJAX?
        # We can use the following code to get the query from AJAX request.
        # query = request.GET.get('query', None)
        # if query is None:
        #     query = request.POST.get('query', None)
        if query:
            search_results = Post.objects.filter(title__icontains=query)
            response_text = ""
            context = {
               'search_results': search_results,
                'query': query
            }
            return render(request, self.template_name, context)
        else:
            message = "No posts found on this topic."
            return HttpResponseRedirect(reverse('posts_page'))

# All future stuff

# The admin can only add authors to the database.
# If you want to delete a post, you can do it from the admin page.
# So far it's only Create and Read views.
# That's the restriction for now.

# What is an UpdateView? It's a generic view that allows you to update a model instance.
# Debug this view.
class EditPostView(UpdateView):
    # We will use this view to edit a post.
    model = Post
    form_class = PostForm
    template_name = 'blog/edit-post.html'
    success_url = reverse_lazy('posts_page')
    # Initial post content to edit
    
    # We want to render the form with the current data of the post.
    def get(self, request, slug):
        post = self.get_object()

        # Get the original data of the post to edit.
        postData = {
        'title': Post.objects.get(slug=slug).title,
        'content': Post.objects.get(slug=slug).content,
        'tag': Post.objects.get(slug=slug).tag.all(),
        'image_name': Post.objects.get(slug=slug).image_name
        }
        form = PostForm(initial=postData)
        context = {
            'form': form,
            'post': post
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        # This method will be called when the form is submitted.
        # We will update the post with the new data.
        form = PostForm(request.POST, request.FILES, instance=self.get_object())
        form.save() # It will update the post with the new data.
        return HttpResponseRedirect(reverse('post_detail_page', args=[slug]))
    # This will be a PUT or a PATCH request.
    # It will update the post with the new data.
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class DeleteObjectView(View):
    '''
    This method will delete a post or a comment based on the content type.
    Delete is a post request because it is sending data to the server.
    '''
    def post(self, request, content):
        if content == 'post':
            post = Post.objects.get(id=request.GET['id'])
            post.delete()
            messages.success(request, "Post deleted successfully.")
            return HttpResponseRedirect(reverse('posts_page'))
        elif content == 'comment':
            comment = Comment.objects.get(id=request.GET['id'])
            comment.delete()
            messages.success(request, "Comment deleted successfully.")
            return HttpResponseRedirect(reverse('post_detail_page', args=[comment.post.slug]))
        else:
            messages.error(request, "Invalid content type.")
            return HttpResponseRedirect(reverse('posts_page'))

# This could be done using a group machine learning algorithm.
# K means clustering algorithm could be used to group the posts based on certain similarities it discovers.
# It'll be nice to have a feature like this in the future which involves some machine learning.
