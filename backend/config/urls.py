from django.contrib import admin
from django.urls import path, include


apipatterns = [
    path("", include("photos.urls")),
    path("", include("users.urls")),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include(apipatterns)),
]
