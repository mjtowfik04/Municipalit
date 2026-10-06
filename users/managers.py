from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, number, password=None, **extra_fields):
        if not number:
            raise ValueError("Phone number is required")

        user = self.model(
            number=number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, number, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(
            number=number,
            password=password,
            **extra_fields
        )