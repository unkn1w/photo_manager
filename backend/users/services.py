from django.contrib.auth import get_user_model

from users.validators import validate_unique_username, validate_unique_email

User = get_user_model()


def user_create(*,
                email: str,
                username: str,
                password: str) -> User:

    validate_unique_username(username)
    validate_unique_email(email)

    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    
    return user
