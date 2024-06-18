from django import forms
from.models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {'user_name' : 'Your Name', 'body': 'Your Thoughts?'}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['slug', 'comment']
        success_url = 'blog/all-posts.html'

        labels = {
            'title': 'Title',
            'image': 'Image for Post Preview',
            'excerpt': 'Short Description',
            'content': 'Tell your Story'
        }
        
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        } # This will create a checkbox for each tag in the form view. And it will allow multiple tags to be selected.
