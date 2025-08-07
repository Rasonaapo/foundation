from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"From {self.name} <{self.email}> at {self.created_at:%Y-%m-%d %H:%M}"


class ContactInfo(models.Model):
    TYPE_CHOICES = [
        ('address', 'Address'),
        ('phone', 'Phone'),
        ('email', 'Email'),
    ]

    info_type = models.CharField(max_length=20, choices=TYPE_CHOICES, unique=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    extra_info = models.CharField(max_length=255, blank=True)  # e.g. business hours for phone
    icon_class = models.CharField(max_length=50, blank=True, help_text='CSS icon class like ti-home, ti-tablet, ti-email')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.get_info_type_display()} Info'
    
    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"
        ordering = ['info_type']
