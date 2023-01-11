from django.urls import path

from users.views import UserCreateApi, UserRetrieveApi


user_patterns = [
    path('user/', UserRetrieveApi.as_view(), name='user_retrieve'),
    path('user/create/', UserCreateApi.as_view(), name='user_create')
]

urlpatterns = user_patterns