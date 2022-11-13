from django.db import models
from tinymce import models as tinymce_models
from django.utils.text import slugify

# Create your models here.
class Property(models.Model):
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=200, blank=True, null=True)
    discount = models.CharField(max_length=200, blank=True, null=True)
    thumbnail = models.FileField(upload_to='thumbnails/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Property'

    def __str__(self):
        return self.location

class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.property.location

class Blog(models.Model):
    thumbnail = models.FileField(upload_to='blog/')
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True)
    content = tinymce_models.HTMLField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Blogs'
        ordering = ["-publish_date"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)