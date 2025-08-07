from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.text import slugify
from django.urls import reverse
from .utils import resize_image

# Create your models here.
class CustomUserManager(BaseUserManager):
    """Manager for CustomUser"""

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a 'CustomUser' with an email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Use the built-in method to hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a 'CustomUser' with superuser permissions."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom User Model"""
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(null=True, default="avatar.png")
    contact = models.CharField(max_length=10, unique=True, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Use email as the username
    REQUIRED_FIELDS = []  # Fields required when creating a user via the createsuperuser command

    def __str__(self):
        return self.email

from django.db import models

class Footer(models.Model):
    left_text = models.TextField("Left/Intro Text", blank=True)
    newsletter_text = models.CharField("Newsletter Text", max_length=255, blank=True)
    contact_address = models.CharField("Contact Address", max_length=255)
    contact_phone = models.CharField("Contact Phone", max_length=50, blank=True)
    contact_email = models.EmailField("Contact Email", blank=True)
    contact_website = models.URLField("Website", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # add social media fields
    facebook_url = models.URLField("Facebook URL", blank=True)
    twitter_url = models.URLField("Twitter URL", blank=True)
    instagram_url = models.URLField("Instagram URL", blank=True)
    linkedin_url = models.URLField("LinkedIn URL", blank=True)
    skype_url = models.URLField("Skype URL", blank=True)
    youtube_url = models.URLField("YouTube URL", blank=True)
    

    def __str__(self):
        return "Site Footer (edit to update site-wide footer info)"

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"
        ordering = ['-created_at']

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='events/')
    event_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True, verbose_name="Expiry Date", help_text="Date after which event is archived and hidden from display")
    categories = models.ManyToManyField(Category, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    archived = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # Automatically archive event if expiry_date passed
        from django.utils import timezone
        if self.expiry_date and self.expiry_date < timezone.now().date():
            self.archived = True
        # Resize the image if it exists
        if self.photo and (not self.pk or self.photo._file):
            self.photo = resize_image(self.photo, max_width=600, max_height=400)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-event_date', '-created_at']
    

class MostTrending(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(help_text="URL to the trending post/video/article")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.TextField(blank=True)
    photo = models.ImageField(upload_to='most_trending/', blank=True, null=True)
    expiry_date = models.DateField(null=True, blank=True, verbose_name="Expiry Date", help_text="Date after which event is archived and hidden from display")
    archived = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # Resize the image if it exists
        if self.photo and (not self.pk or self.photo._file):
            self.photo = resize_image(self.photo, max_width=600, max_height=400)

        # Automatically archive trending if expiry_date passed
        from django.utils import timezone
        if self.expiry_date and self.expiry_date < timezone.now().date():
            self.archived = True
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Returns the external URL directly since it points to external media
        return self.url

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Most Trending"
        verbose_name_plural = "Most Trending"
        ordering = ['-created_at']
    
