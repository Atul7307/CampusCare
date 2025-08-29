from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'student', 'Student'
        COUNSELLOR = 'counsellor', 'Counsellor'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
        help_text="User role determining access level",
    )

    class Meta:
        # Ensure the custom user continues to use the canonical auth table name
        # so the role field lives in the `auth_user` table in Postgres.
        db_table = 'auth_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
