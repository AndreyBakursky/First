from django.db import models

class Articles(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length = 120)
    post = models.TextField()
    date = models.DateTimeField()


    def __str__(self):
        return self.title
