from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from books.constants import USER_ROLES, ADMIN, SUPERADMIN, GUEST
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, email, first_name="", last_name="", **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, cur_city=city, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, email, first_name, last_name):
        return self._create_user(username, password, email, first_name, last_name)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('roles', ADMIN)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, email, **extra_fields)

    def managers(self):
        return User.objects.filter(roles=SUPERADMIN)

    def directors(self):
        return User.objects.filter(roles=GUEST)


class User(AbstractUser):
    roles = models.CharField(choices=USER_ROLES, default=GUEST, max_length=150, null=True, blank=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['roles', 'username', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')
    bio = models.TextField(max_length=500, blank=True, verbose_name='Информация')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'