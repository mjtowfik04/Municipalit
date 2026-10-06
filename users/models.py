from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from wards.models import Wards
from users.managers import UserManager

class User(AbstractUser):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    ROLE_CHOICES = [
        ("citizen", "Citizen"),
        ("officer", "Officer"),
        ("admin", "Admin"),
    ]

    # AbstractUser-এর username বাদ দেওয়া
    username = None

    email = models.EmailField()

    number = PhoneNumberField(
        unique=True,
        region="BD"
    )

    ward = models.ForeignKey(
        Wards,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    nid = models.CharField(
        max_length=20,
        unique=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="citizen"
    )

    USERNAME_FIELD = "number"
    REQUIRED_FIELDS = []
    objects = UserManager()


    def __str__(self):
        return self.email