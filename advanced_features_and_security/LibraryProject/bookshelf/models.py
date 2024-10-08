from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField()


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError("User must have an email")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    
    class Meta:
        permissions = [
            ("can_create", "Can create Books"),
            ("can_view", "Can read books"),
            ("can_edit","Can edit books"),
            ("can_delete","Can delete books")
        ]

