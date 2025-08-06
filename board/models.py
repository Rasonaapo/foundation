from django.db import models
from core.utils import resize_image

class Director(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='directors/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    TEAM_TYPE_CHOICES = (
        ('trustee', 'Trustee'),
        ('management', 'Management')
    )
    team_type = models.CharField(max_length=20, choices=TEAM_TYPE_CHOICES, default='trustee')
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first")

    # add social media links 
    facebook_url = models.URLField("Facebook URL", blank=True)
    twitter_url = models.URLField("Twitter URL", blank=True)
    instagram_url = models.URLField("Instagram URL", blank=True)
    linkedin_url = models.URLField("LinkedIn URL", blank=True)
    skype_url = models.URLField("Skype URL", blank=True)
    youtube_url = models.URLField("YouTube URL", blank=True)

    def save(self, *args, **kwargs):
        if self.photo and (not self.pk or self.photo._file):
            self.photo = resize_image(self.photo, max_width=600, max_height=400)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.name} ({self.role})" if self.role else self.name
