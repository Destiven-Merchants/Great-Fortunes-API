from django.contrib import admin
from properties.models import Property, PropertyImages, Blog

# Register your models here
class PropertyImagesAdmin(admin.StackedInline):
    model = PropertyImages

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImagesAdmin]

    class Meta:
        model = Property

@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    model = Blog

    list_display = (
        "id",
        "title",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "slug",
        "content",
    )
    prepopulated_fields = {
        "slug": (
            "title",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True