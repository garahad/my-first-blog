from django.db import models

# Create your models here.

class Entries(models.Model):
    Title = models.CharField(max_length=80, null=False)
    Content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    Category = models.ForeignKey(Categories)
    Tags = models.ManyToManyField(TagModel)
    Comments = models.PositiveSmallIntegerField(default=0, null=True)

    class Admin:
    	pass