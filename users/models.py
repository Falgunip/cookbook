from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, mobile_no, date_of_birth, age, country, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email), # Normalize the email address by lowercasing the domain part of it.
            first_name=first_name,
            last_name=last_name,
            mobile_no=mobile_no,
            date_of_birth=date_of_birth,
            age=age,
            country=country,
            )
        user.set_password(password)
        user.save(using=self._db) # takes its default value is specified in settings.py
        return user

    def create_superuser(self, email, first_name, last_name, mobile_no, date_of_birth, age, country, password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            mobile_no=mobile_no,
            age=age,
            date_of_birth=date_of_birth,
            country=country,
        )
        user.is_admin=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=255,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=255,
    )
    mobile_no = models.IntegerField(
        verbose_name='mobile no',
    )
    date_of_birth = models.DateField()
    age = models.IntegerField()
    country = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    # when you are changing authentication from username to email, you need to write below line. It means authentication happens through email field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'country', 'first_name', 'last_name', 'mobile_no', 'age']

    def __str__(self):
        return self.email

    #https://docs.djangoproject.com/en/1.8/ref/contrib/auth/#django.contrib.auth.backends.ModelBackend.has_perm
    # Uses get_all_permissions() to check if user_obj has the permission string perm. Returns False if the user is not is_active.
    def has_perm(self, perm, obj=None):
        return True

    # Returns whether the user_obj has any permissions on the app app_label.
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin







