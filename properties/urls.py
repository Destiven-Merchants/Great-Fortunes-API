from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from properties import views

urlpatterns = [
    path('property', views.PropertyView.as_view()),
    path('property/<str:id>/', views.SinglePropertyView.as_view()),
    path('propertyimages/<str:id>', views.PropertyImagesView.as_view()),
    path('blogs', views.BlogView.as_view()),
    path('blogpost/<str:slug>', views.BlogPostView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)