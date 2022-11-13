from rest_framework.response import Response
from properties.serializers import PropertySerializer, PropertyImagesSerializer, BlogSerializer
from properties.models import Property, PropertyImages, Blog
from rest_framework import generics, permissions

# Create your views here.
class BlogView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Blog.objects.all()

class BlogPostView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, slug):
        res = []
        post = Blog.objects.get(slug=slug)
        serializer = BlogSerializer(post)
        res.append(serializer.data)
        return Response(res)

class PropertyView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Property.objects.all()

class SinglePropertyView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, id):
        res = []
        plot = Property.objects.get(pk=id)
        serializer = PropertySerializer(plot)
        res.append(serializer.data)
        return Response(res)

class PropertyImagesView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PropertyImagesSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, id):
        res = []
        property_images = PropertyImages.objects.filter(property__id=id)
        for images in property_images:
            serializer = PropertyImagesSerializer(images)
            res.append(serializer.data)
        return Response(res)