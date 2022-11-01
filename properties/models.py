from django.db import models

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