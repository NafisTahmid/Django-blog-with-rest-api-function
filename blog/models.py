from django.db import models
from django.utils.text import slugify 

# Create your models here.
class BlogCategory(models.Model):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(unique = True, blank = True, null = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            slug_number = 1
            slug_object = self.slug
            if BlogCategory.objects.filter(slug = self.slug).exists():
                self.slug = f"{slug_object}-{slug_number}"
                slug_number += 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique = True, blank = True, null = True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            slug_number = 1
            slug_object = self.slug
            if Blog.objects.filter(slug = self.slug).exists():
                self.slug = f"{slug_object}-{slug_number}"
                slug_number += 1
        super().save(*args, **kwargs)

    def __str__ (self):
        return self.title
