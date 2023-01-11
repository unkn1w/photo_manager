from photos.models import Photo

def create_photo(data):
    return Photo.objects.create(**data)
