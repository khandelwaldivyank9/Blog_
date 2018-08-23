
from django.db import models

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User',null=True, related_name='blogs', on_delete=models.CASCADE)

    def __str__(self):
        return self.author