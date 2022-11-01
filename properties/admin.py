from django.contrib import admin
from properties.models import Property, PropertyImages

# Register your models here
class PropertyImagesAdmin(admin.StackedInline):
    model = PropertyImages

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImagesAdmin]

    class Meta:
        model = Property
