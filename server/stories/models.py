import datetime

from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Story(models.Model):
    DRAFT = 0
    PUBLISHED = 1
    STATUSES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    THRILLER = 0
    ROMANCE = 1
    COMEDY = 2
    GENRES = (
        (THRILLER, 'Thriller'),
        (ROMANCE, 'Romance'),
        (COMEDY, 'Comedy'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='story')
    status = models.IntegerField(choices=STATUSES, default=DRAFT)
    genre = models.IntegerField(choices=GENRES, default=COMEDY)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True, blank=True)
    live = models.BooleanField(default=False)

    # num_votes
    # author


    # def get_absolute_url(self):
    #     return reverse('story:story_detail', args={'pk': self.pk})


    def __str__(self):
        return self.title