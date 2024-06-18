from django import forms
from.models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': 'What are your thoughts?'}

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
