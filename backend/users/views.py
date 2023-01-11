from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import status, filters, generics
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from users.serializers import UserCreateSerializer, UserRetrieveSerializer
from users.services import user_create
from users.selectors import get_user

User = get_user_model()


class UserCreateApi(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request) -> Response:
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user_create(**serializer.validated_data)
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)


class UserRetrieveApi(generics.RetrieveAPIView):
    serializer_class = UserRetrieveSerializer

    def get(self, request):
        user = get_user(request.user.id)
        serializer = UserRetrieveSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
