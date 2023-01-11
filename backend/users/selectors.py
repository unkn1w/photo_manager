from django.contrib.auth import get_user_model
from django.db.models import QuerySet

User = get_user_model()


def get_user(id: int) -> QuerySet[User]:
    return User.objects.get(id=id)
