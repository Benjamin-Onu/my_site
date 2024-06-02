from django.db import models
from django.core.validators import MinLengthValidator

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
    image_name = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)]) 
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts') # one author can have many posts
    tag = models.ManyToManyField(Tag, related_name='tags') # one post can have many tags



 
