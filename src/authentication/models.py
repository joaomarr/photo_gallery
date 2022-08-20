from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_friend, is_superuser, is_staff, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_friend=is_friend,
            is_superuser=is_superuser,
            is_staff=is_staff,
            last_login=timezone.now(),
            registered_at=timezone.now(),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        is_friend = extra_fields.pop('is_friend', True)
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)
        return self._create_user(username, email, password, is_friend, is_superuser, is_staff, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(
            username, email, password, is_friend=False, is_superuser=True, is_staff=True, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(verbose_name='Username', unique=True, max_length=255)
    email = models.EmailField(verbose_name='Email', blank=True, max_length=255)
    first_name = models.CharField(verbose_name='First name', blank=True, max_length=100)
    last_name = models.CharField(verbose_name='Last name', blank=True, max_length=100)
    is_active = models.BooleanField(verbose_name='Active', default=True)

    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    is_superuser = models.BooleanField(verbose_name='superuser', default=False)
    is_friend = models.BooleanField(verbose_name='Friend', default=True)
    registered_at = models.DateTimeField(verbose_name='Registered at', auto_now_add=timezone.now)

    # Fields settings
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
