from django import forms
from blogSite.models import Post,Comments

class PostForm(forms.ModelForm):

    class Meta:
        models = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-text post content'})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        models = Comments
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-text'})
        }


