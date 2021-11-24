from django.db import models


class Headline(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title
