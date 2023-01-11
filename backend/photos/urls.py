from django.urls import path

from photos.views import PhotoUploadApi, PhotoMetaListApi, PhotoListApi, PhotoRetrieveApi


photo_patterns = [
    path('photo/upload/', PhotoUploadApi.as_view(), name='photo_upload'),
    path('photo/<int:pk>/', PhotoRetrieveApi.as_view(), name='photo'),
    path('photos/', PhotoListApi.as_view(), name='photos'),
    path('photos/detailed/', PhotoMetaListApi.as_view(), name='photos_detailed'),
]

urlpatterns = photo_patterns