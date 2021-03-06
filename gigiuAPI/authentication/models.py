from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
# Create your models here.


class UserManager(BaseUserManager):
    """
    Creates and saves a User with the given email and password
    """

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password
        """
        user = self.create_user(email, password=password,)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(email, password=password,)

        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & password are required by default

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        """ Does the user have a specific permission? """
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """ Does the user have permission to view the app 'app_label' """
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """ Is the user a member of staff? """
        # Simplest possible answer: All admins are staff
        return self.staff

    @property
    def is_admin(self):
        """ Is the user a admin member?"""
        return self.admin
