from django.db import models

# Create your models here.
class Url(models.Model):
    hash_url =models.SlugField(max_length=100, blank=False)
    actual_url = models.SlugField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.hash_url
