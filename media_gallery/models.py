from django.db import models
from core.utils import resize_image

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    expires_at = models.DateField(null=True, blank=True, help_text="Date to remove/hide image (optional)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Resize only on new upload or changed file
        if self.image and (not self.pk or self.image._file):
            self.image = resize_image(self.image, max_width=1200, max_height=900)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        ordering = ['-created_at']

    def __str__(self):
        return self.caption or f"Image {self.pk}"
    



class MarqueeImage(models.Model):
    image = models.ImageField(upload_to='marquee/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):    
        if self.image and (not self.pk or self.image._file):
            self.image = resize_image(self.image, max_width=600, max_height=400)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Marquee Image"
        verbose_name_plural = "Marquee Images"
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.caption or f"Marquee {self.pk}"
