from django.db import models as md


class Headline(md.Model):
    date = md.DateTimeField(auto_now_add=True)
    title = md.CharField(max_length=200)
    image = md.URLField(null=True, blank=True)
    url = md.TextField()

    def __str__(self):
        return self.title
