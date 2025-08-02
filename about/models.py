from django.db import models


class Mission(models.Model):
    text = models.TextField("Mission Statement")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mission"
        verbose_name_plural = "Mission Statements"

    def __str__(self):
        return self.text[:60]

class Vision(models.Model):
    text = models.TextField("Vision Statement")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vision"
        verbose_name_plural = "Vision Statements"

    def __str__(self):
        return self.text[:60]

class Value(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Value"
        verbose_name_plural = "Values"
        ordering = ['name']

    def __str__(self):
        return self.name
