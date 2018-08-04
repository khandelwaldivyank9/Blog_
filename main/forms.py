from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ['user']

    error_message={'title_length':'Title should have atleast 50 words',
                   'description_length':'Description should have atleast 200 words'}

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title)<50:
            raise forms.ValidationError(self.error_message['title_length'])
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description)<200:
            raise forms.ValidationError(self.error_message['description_length'])
        return description

