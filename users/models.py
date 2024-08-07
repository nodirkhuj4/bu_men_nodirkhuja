from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class UserCreateManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    class Language(models.TextChoices):
        UZ = "UZ", "UZBEK"
        RU = "RU", "RUSSIAN"

    phone_number = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=64)
    balance = models.PositiveBigIntegerField(default=50000)
    is_pro = models.BooleanField(default=False)
    pro_finish_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2, 
                                choices=Language.choices, default=Language.UZ)
    score = models.PositiveBigIntegerField()

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserCreateManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'




