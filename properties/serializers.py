from rest_framework import serializers
from properties.models import Property, PropertyImages, Blog

class PropertyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImages
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'