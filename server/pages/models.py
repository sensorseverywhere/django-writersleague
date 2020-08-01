from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class PageTemplateTagManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class PageTemplateTag(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return (self.name)


class ContentBlockManager(models.Model):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class ContentBlock(models.Model):
    tags = models.ForeignKey(PageTemplateTag, on_delete=models.CASCADE, to_field='name')
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
    	return self.title
    
    def natural_key(self):
        return (self.title)


class ContentBlockImage(models.Model):
    cb = models.ForeignKey(ContentBlock, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.image


class NewsItem(models.Model):
    url = models.CharField(max_length=256)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    image_url = models.CharField(max_length=256)
    active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
