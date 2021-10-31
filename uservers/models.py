from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
# create user using manageer


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email field is mandetory")
        if not username:
            raise ValueError("Must Enter valid username")
        user = self.model(
            email=email,
            username=username,

        )
        user.set_password(password)
        user.save(using="user")
        return user

# create superuser
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using="user")
        return user


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(verbose_name="FirstName", max_length=255, null=True)
    last_name = models.CharField(verbose_name="LastName", max_length=255, null=True)
    email = models.EmailField(verbose_name="E-mail",max_length=100, unique=True, blank=False)
    username = models.CharField(verbose_name="Username", max_length=40, unique=True, blank=False)
    password = models.CharField( verbose_name="Password", max_length=100, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.user.email