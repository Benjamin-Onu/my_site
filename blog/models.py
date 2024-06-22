from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify


# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField() # check documentation for more validation options
    # bio = models.TextField()
    
    def full_name(self):
        'return the full name of the author'
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        'return the string representation of the author object'
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='static/blog/images/') # upload_to is the directory where the image will be saved, upload_to will handle file uploads
    image_name = models.ImageField(upload_to='posts', null=True) # upload_to is the directory where the image will be saved, upload_to will handle file uploads
    # to display the image in the template, we can use the following code: use the url attribute of the image field to display the image in the template. # <img src="{{ post.image.url }}" alt="{{ post.title }}">
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)]) 
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts') # one author can have many posts
    tag = models.ManyToManyField(Tag, related_name='tags') # one post can have many tags

    def __str__(self):
        return self.title
    
    # TO do
    # We have to slugify the title field to create a unique slug for each post.
    # We can use the slugify function from django.utils.text to create a slug from the title. 
    # This will create a slug when the form is saved.
    def save(self, *args, **kwargs):
        # self.slug = self.title.lower().replace(" ", "-")
        # slugify() function is used to create a slug from the title
        # slugify() function takes a string and returns a slugified version of it.
        # slugify() function replaces spaces with hyphens and converts the string to lowercase.
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # args and kwargs are used to pass arguments to the parent class's save() method.


# We would also like to add a feature to allow users to comment on posts. This can be done using a comment form on each post. We can create a comment model and a comment form on the post.html file. The comment form will submit the comment to the database.

# We would introduce another model for comments. This would be a one-to-many relationship between posts and comments. 
# And it will include fields like name, email, and content. It will be implemented using modelForms.

class Comment(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True) # this name will normally be the user account name but they will enter their name manually.
    body = models.TextField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True) # there's total participation on the comment side of the relationship hence null values on the post field is not allowed. Django doesn't let us implement this.
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
