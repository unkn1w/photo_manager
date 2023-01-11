from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=255, blank=True)
    people = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    meta_data = models.JSONField()

    def __str__(self) -> str:
        return f'Image {self.user}, Date: {self.date}'
