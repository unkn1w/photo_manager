from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from photos.serializers import PhotoMetaSerializer, PhotoSerializer
from photos.permissions import IsObjectOwner
from photos.selectors import get_photo, get_user_photos
from photos.services import create_photo


class PhotoUploadApi(generics.CreateAPIView):

    permission_classes = [IsAuthenticated | IsAdminUser]
    serializer_class = PhotoMetaSerializer

    def post(self, request) -> Response:
        serializer = PhotoMetaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        data['user'] = request.user

        create_photo(data)

        return Response(status=status.HTTP_201_CREATED)


class PhotoRetrieveApi(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated & IsObjectOwner | IsAdminUser]
    serializer_class = PhotoMetaSerializer

    def get(self, request, pk) -> Response:
        photo = get_photo(id=pk)
        serializer = PhotoMetaSerializer(photo)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PhotoMetaListApi(generics.ListAPIView):

    serializer_class = PhotoMetaSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'people', 'place', 'date']
    search_fields = ['^people']

    def get_queryset(self):
        return self.filter_queryset(get_user_photos(user=self.request.user))

    def list(self, request) -> Response:
        queryset = self.get_queryset()
        serializer = PhotoMetaSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PhotoListApi(generics.ListAPIView):

    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'people', 'place', 'date']
    search_fields = ['^people']

    def get_queryset(self):
        return self.filter_queryset(get_user_photos(user=self.request.user))

    def list(self, request) -> Response:
        queryset = self.get_queryset()
        serializer = PhotoSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
