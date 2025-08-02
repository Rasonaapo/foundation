from django.db import models
from core.utils import resize_image

class Director(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='directors/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.photo and (not self.pk or self.photo._file):
            self.photo = resize_image(self.photo, max_width=600, max_height=400)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Board of Directors"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.role})" if self.role else self.name
