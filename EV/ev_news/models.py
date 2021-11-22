from django.db import models as md


class NewsModel(md.Model):

    title = md.CharField(max_length=255,)
    content = md.TextField()
    photo = md.ImageField(upload_to="potos/%Y/%m/%d/")
    time_create = md.DateTimeField(auto_now_add=True,)
    time_update = md.DateTimeField(auto_now=True,)
    is_published = md.BooleanField(default=True,)
