from rest_framework import serializers

from photos.models import Photo
from users.serializers import UserRetrieveSerializer


class PhotoMetaSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer(read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'user', 'image', 'date', 'place', 'people', 'description', 'meta_data']


class PhotoSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer(read_only=True)
    
    class Meta:
        model = Photo
        fields = ['id', 'user', 'image']
