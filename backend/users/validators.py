from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


def validate_unique_username(username: str) -> None:
    if User.objects.filter(username=username).exists():
        raise ValidationError("User with this username was already created!")

def validate_unique_email(email: str) -> None:
    if User.objects.filter(email=email).exists():
        raise ValidationError("User with this email was already created!")