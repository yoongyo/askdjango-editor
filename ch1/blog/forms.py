from .models import Post
from django import forms
from .widgets import TuiEditorWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'content',
            'message',
        ]
        widgets = {
            'message': TuiEditorWidget,
        }
        exclude = ()

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post


