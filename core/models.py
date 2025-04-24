from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    
)
from django.contrib.auth import get_user_model
from django.db import models


class UserManager(BaseUserManager):
    """Mamager for users"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must provide an email ....')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create superusers """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.level = 0
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    level = models.PositiveSmallIntegerField(verbose_name="user level", default=9999)
    objects = UserManager()
    USERNAME_FIELD = 'email'

class Owner(models.Model):
    """Create a owner model"""
    user = models.ForeignKey(
        get_user_model(),
        related_name='owner',
        on_delete=models.CASCADE
        )
    
    def __str__(self):
        return self.user.email


class OwnerProfile(models.Model):
    """Create a Profile Model for the owner """
    owner = models.OneToOneField(Owner, related_name='owner_profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=200, blank=True, null=True, default="Earth")
    short_intro = models.CharField(max_length=200, blank=True, null=True, default="This is a default intro. User has not added a intro.")
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name:
            return self.name
        return self.owner.user.email
    def get_image_url(self):
        if self.profile_image:
            return self.profile_image.url
        return 'images/profiles/default.jpg'
