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
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
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


class UserContactApplication(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, unique=True)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('User Contact Application')
        verbose_name_plural = _('User Contact Applications')
        db_table = 'user_contact_application'
        ordering = ['-created_at']


