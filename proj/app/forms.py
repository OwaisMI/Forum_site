from django import forms
from app.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('author','title','text')

    widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
    }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields= ('author','text')