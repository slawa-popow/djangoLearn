from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['-title']),
        ]

    def get_fields(self) -> tuple:
        return (self.title, self.content, str(self.time_create), str(self.time_update), self.is_published,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})