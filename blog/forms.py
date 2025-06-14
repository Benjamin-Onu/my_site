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
        # we want to see if the author can be the logged in user. 
        
        labels = {
            'title': 'Title',
            'excerpt': 'Short Description',
            'content': 'Tell your Story'
        }
    
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        } # This will create a checkbox for each tag in the form view. And it will allow multiple tags to be selected.


# env/Scripts/activate
# There will be a separate form to add an image for the post preview. That will be after the post is created. It will be an update form.
class PostImageForm(forms.Form):
    image = forms.ImageField()
