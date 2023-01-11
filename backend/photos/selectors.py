from django.db.models import QuerySet
from django.contrib.auth import get_user_model

from photos.models import Photo

User = get_user_model()

def get_photo(id: int) -> QuerySet[Photo]:
    return Photo.objects.get(id=id)

def get_user_photos(user: User) -> QuerySet[Photo]:
    return Photo.objects.filter(user=user)
