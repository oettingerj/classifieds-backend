from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, google_account_id, email, given_name, last_name, role):
        new_user = self.model (
            google_account_id = google_account_id,
            email = email,
            given_name = given_name,
            last_name = last_name,
            role = role,
        )

        new_user.set_unusable_password()
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, google_account_id, email, given_name, last_name, role, password=None):
        new_superuser = self.model (
            google_account_id = google_account_id,
            email = email,
            given_name = given_name,
            last_name = last_name,
            is_superuser = True,
            role = role,
        )

        new_superuser.set_password(password)
        new_superuser.save(using=self._db)
        return new_superuser

class User(AbstractBaseUser, PermissionsMixin):
    #password field and last_login field inhereted from AbstractBaseUser
    USERNAME_FIELD = 'google_account_id'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['given_name', 'last_name', 'email', 'role']

    google_account_id = models.TextField(default="no id", unique=True)
    email = models.EmailField(unique=True)
    given_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=150)
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    roleChoice = models.TextChoices('roleChoice', 'STUDENT FACULTY STAFF ALL')
    role = models.CharField(choices=roleChoice.choices, max_length=7)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

    def get_full_name(self):
        return given_name + " " + last_name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_name):
        return True

    def __str__(self):
        description = "Google ID: " + self.google_account_id + " " + "Last name: " + self.last_name
        return description
