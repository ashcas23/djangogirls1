from django import forms
from django.core.exceptions import ValidationError
from .models import Post
class PostForm(forms.ModelForm):

    def clean(self):
        clean_data = super().clean()
        if Post.objects.filter(title = clean_data.get("title", "")).exists(): #filtering all the posts in database to see if any posts matches other title posts from the request
            raise ValidationError ("Post already has existing title") #
        return clean_data

    class Meta:
        model = Post
        fields = ('title', 'text',)
