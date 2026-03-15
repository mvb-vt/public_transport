from django.core import exceptions, validators
from django.db import models
from django.contrib.auth import models as auth_models


def validate_name_is_alphabetic(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Names must only contain letters')


class Status(models.TextChoices):
    CHILD = 'CHILD', 'CHILD',
    STUDENT = 'STUDENT', 'STUDENT',
    REGULAR = 'REGULAR', 'REGULAR',
    PENSION = 'PENSION', 'PENSION',
    TOURISM = 'TOURISM', 'TOURISM',

class UserProfiles(auth_models.AbstractUser):

    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    email = models.EmailField(
        unique=True
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            validate_name_is_alphabetic,
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH)
        ]
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            validate_name_is_alphabetic,
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH)
        ]
    )
    birth_date = models.DateField(
        null=True, blank=True,
    )

    phone_number = models.CharField(
        max_length=20, null=True, blank=True,
    )

    status = models.CharField(
        choices=Status,
        default=Status.CHILD,
    )
